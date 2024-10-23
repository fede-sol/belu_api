from rest_framework import generics, permissions, status
from rest_framework.response import Response
from belu_auth.models import BeluUserProfile
from .models import Payment, Reservation
from .serializers import PaymentSerializer, ReservationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserReservationListCreateView(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['start_date', 'end_date', 'room__hotel']

    def get_queryset(self):
        return Reservation.objects.filter(user_profile__user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            request.data['user_profile'] = request.user.belu_user_profile.id
        except BeluUserProfile.DoesNotExist:
            return Response({'detail': 'User profile not found'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.belu_user_profile)

class ReservationDetailView(generics.RetrieveAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Reservation.objects.filter(id=self.kwargs['pk'], user_profile__user=self.request.user)

class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Payment.objects.filter(reservation__user_profile__user=self.request.user)

class PaymentListByReservationView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Payment.objects.filter(reservation__id=self.kwargs['pk'], reservation__user_profile__user=self.request.user)
