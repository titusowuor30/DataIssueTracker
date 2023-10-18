# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from django.contrib.auth import authenticate, login
from .models import CustomUser
from DQIT_Endpoint.models import Facilities
from .serializers import CustomUserSerializer
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.pagination import LimitOffsetPagination
from django.http import Http404

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
    authentication_classes=()

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

class UserApiView(APIView):

    def process_issues(self, data):
        for id in data:
            yield id  # Yield the processed ID, for memory effieciency in case of big data

    def post(self, request, format=None):
        ids = request.data['data_ids']
        processed_ids=self.process_issues(ids)
        #print(list(processed_ids))
        for id in processed_ids:
            issue = self.get_object(id)
            issue.action_taken =request.data['action']
            issue.save()
        return Response('success!', status=status.HTTP_201_CREATED)

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            user=self.get_object(pk)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)

        query_params = request.query_params
        username = query_params.get('username',None)
        email = query_params.get('email',None)
        country = query_params.get('country',None)

        users = CustomUser.objects.filter(email=request.user.email) if request.user.role.role_name !='Admin' else CustomUser.objects.all()

        if username:
            users = users.filter(username=username)
        if email:
            users = users.filter(email=email)
        if country:
            users = users.filter(country=country)

        paginator = LimitOffsetPagination()
        paginator.default_limit = 100
        result_page = paginator.paginate_queryset(users, request)
        serializer = CustomUserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        if user:
            user.username=request.data['username']
            user.save()
            return Response('Success!')
        return Response('Error updating issue', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        issue = self.get_object(pk)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        # Serialize the user data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract all the fields from the request data
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        role = serializer.validated_data.get('role')
        gender = serializer.validated_data.get('gender')
        profile_pic = serializer.validated_data.get('profile_pic')
        phone = serializer.validated_data.get('phone')
        address = serializer.validated_data.get('address')
        facilities = serializer.validated_data.get('facilities')
        fcm_token = serializer.validated_data.get('fcm_token')

        # Create the user with the provided fields
        user,created= CustomUser.objects.get_or_create(
            email=email,
            defaults={
            'email':email,
            'password':password,
            'role':role,
            'gender':gender,
            'profile_pic':profile_pic,
            'phone':phone,
            'address':address,
            'fcm_token':fcm_token,
            }
            )
        user.is_active=False
        user.facilities.set(facilities)
        user.save()

        # Serialize the created user
        serializer = self.get_serializer(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
