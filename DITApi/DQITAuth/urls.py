# urls.py
from django.urls import path,include
from .views import RegistrationAPIView, LoginAPIView, UserApiView,CustomUserViewSet,get_client_info,PasswordPolicyView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('usersapi/', UserApiView.as_view(), name='user'),
    path('user/clientinfo/', get_client_info, name='userinfo'),
    path('password-policy/', PasswordPolicyView.as_view(), name='password-policy'),
    path('', include(router.urls)),
]
