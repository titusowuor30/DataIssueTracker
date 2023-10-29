# urls.py
from django.urls import path,include
from .views import (
    RegistrationAPIView, 
    LoginAPIView, UserApiView,
    CustomUserViewSet,get_client_info,
    PasswordPolicyView,AccountRequestView,
    UserLogAPIs)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('usersapi/', UserApiView.as_view(), name='user'),
    path('usersapi/<int:pk>/', UserApiView.as_view(), name='user'),
    path('user/clientinfo/', get_client_info, name='userinfo'),
    path('password-policy/', PasswordPolicyView.as_view(), name='password-policy'),
    path('account-requests/', AccountRequestView.as_view(), name='account-requests'),
    path('user-logs/', UserLogAPIs.as_view(), name='user-logs'),
    path('user-logs/<int:pk>/', UserLogAPIs.as_view(), name='user-logs'),
    path('', include(router.urls)),
]
