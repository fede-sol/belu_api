from rest_framework import generics, permissions
from .models import Reservation
from .serializers import ReservationSerializer
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

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.belu_user_profile)

class ReservationDetailView(generics.RetrieveAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Reservation.objects.filter(user_profile__user=self.request.user)
