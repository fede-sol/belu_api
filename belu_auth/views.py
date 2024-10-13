from rest_framework.response import Response
from belu_auth.models import BeluUser
from .serializers import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_user_model().objects.get(email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()
            token = CustomTokenObtainPairSerializer().get_token(user)
            return Response({
                'refresh': str(token),
                'access': str(token.access_token),
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'expires_in': int(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds())
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = get_user_model().objects.get(email=request.data['email'])
            response = super().post(request, *args, **kwargs)
        except BeluUser.DoesNotExist:
            response = Response(
                {'detail': 'No user with this email exists.'},
                status=status.HTTP_404_NOT_FOUND
            )
        return response