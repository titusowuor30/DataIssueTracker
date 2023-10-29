# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from django.contrib.auth import authenticate, login
from .models import CustomUser,PasswordPolicy,AccountRequest,UserLog
from DQIT_Endpoint.models import Facilities
from .serializers import CustomUserSerializer,PasswordPolicySerializer,AccountRequestSerializer,UserLogSerializer
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.pagination import LimitOffsetPagination
from django.http import Http404
import socket
from DQIT_Endpoint.modules.custom_email_backend import DQITSEmailBackend
from django.http import HttpResponse
from django.http import JsonResponse
from user_agents import parse
import threading
from .models import Roles
import json

def get_client_info(request):
    client_ip = request.META.get('REMOTE_ADDR', None)

    # Parse the user-agent string to get device and OS information
    user_agent = request.META.get('HTTP_USER_AGENT', None)
    if user_agent:
        user_agent_info = parse(user_agent)
        device = user_agent_info.device.family
        os = user_agent_info.os.family
        if device =='Other':
            device='Unknown Computer'
    # Perform your authentication and login logic here

    # Respond to the client or store the information as needed
    response = {"ip:":client_ip,"device:":device,"os:": os}
    return JsonResponse(response)


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

            #Notify user 
            res=get_client_info(request)
            content=res.content
            clientdata=list(json.loads(content.decode('utf-8')).values())
            print("client data",clientdata)
            if (user.ip_address not in clientdata) or (user.device not in clientdata):
               try:
                    print("Processing login mail")
                    subject="New device just logged into your account"
                    message=f"A new device just logged into your account<br/>\n\nDevice name:{clientdata[1]}<br/>\nDevice OS:{clientdata[2]}<br/>\nIP Address:{clientdata[0]}"
                    # emailthread=threading.Thread(target=DQITSEmailBackend(request=request,subject=subject,body=message,to=["titusowuor30@gmail.com",],attachments=[]).send_email(),name='EmailThread')
                    # emailthread.daemon=True
                    #emailthread.start()
                    print("Email thread started!")
               except Exception as e:
                   print(e)

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
            print(request.data.get('first_name'))
            user.username = request.data.get('username',None)
            user.email = request.data.get('email', None)
            user.first_name = request.data.get('first_name', None)
            user.last_name = request.data.get('last_name', None)
            
            # Assuming 'role' is a ForeignKey relationship
            role_data = request.data.get('role',user.role)
            if role_data:
                role=Roles.objects.get(role_name=role_data)
                user.role = role

            print(request.data.get('phone'))
            
            user.phone = request.data.get('phone', None)
            user.gender = request.data.get('gender', None)
            user.profile_pic = request.data.get('profile_pic', None)
            user.fcm_token = request.data.get('fcm_token', user.fcm_token)
            user.organisation = request.data.get('organisation', user.organisation)
            user.address = request.data.get('address', user.address)
            user.country = request.data.get('country', user.country)
            user.state = request.data.get('state', user.state)
            user.zip = request.data.get('zip', user.zip)
            user.timezone = request.data.get('timezone', user.timezone)
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


class PasswordPolicyView(APIView):
    def get(self, request):
        try:
            policy = PasswordPolicy.objects.first()
            serializer = PasswordPolicySerializer(policy)
            return Response(serializer.data)
        except PasswordPolicy.DoesNotExist:
            return Response({"error": "Password policy settings not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            policy = PasswordPolicy.objects.first()
            serializer = PasswordPolicySerializer(policy, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PasswordPolicy.DoesNotExist:
            return Response({"error": "Password policy settings not found."}, status=status.HTTP_404_NOT_FOUND)



class AccountRequestView(APIView):
    def get(self, request):
        # Retrieve and list all account requests
        account_requests = AccountRequest.objects.all()
        serializer = AccountRequestSerializer(account_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new account request
        serializer = AccountRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogAPIs(APIView):
    def process_issues(self, data):
        for id in data:
            yield id  # Yield the processed ID, for memory effieciency in case of big data

    def post(self, request, format=None):
        data=request.data
        if data['command'] == 'create':
            log = UserLog(user=request.user,action=data['action'])
            log.save()
        else:
            ids = request.data['data_ids']
            processed_ids=self.process_issues(ids)
            #print(list(processed_ids))
            for id in processed_ids:
                log = self.get_object(id)
                log.delete()
        return Response('success!', status=status.HTTP_201_CREATED)

    def get_object(self, pk):
        try:
            return UserLog.objects.get(pk=pk)
        except UserLogSerializer.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            log=self.get_object(pk)
            serializer = UserLogSerializer(log)
            return Response(serializer.data)

        query_params = request.query_params
        user = query_params.get('user',None)
        action = query_params.get('action',None)
        timestamp = query_params.get('timestamp',None)

        logs = UserLog.objects.filter(user=request.user) if request.user.role.role_name !='Admin' else UserLog.objects.all()

        if user:
            logs = logs.filter(user=user)
        if action:
            logs = logs.filter(action=action)
        if timestamp:
            logs = logs.filter(timestamp=timestamp)

        paginator = LimitOffsetPagination()
        paginator.default_limit = 100
        result_page = paginator.paginate_queryset(logs, request)
        serializer = UserLogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def delete(self, request, pk, format=None):
        log = self.get_object(pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
