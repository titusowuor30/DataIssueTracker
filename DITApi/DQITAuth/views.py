# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class RegistrationAPIView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = ()

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)

            # Fetch user's roles
            role = user.role.role_name if user.role else None

            # Serialize user data
            user_serializer = CustomUserSerializer(user)
            user_data = user_serializer.data
            user_data['role'] = role  # Add roles to user data

            return Response({"token": token.key, "user": user_data}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserAPIView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
