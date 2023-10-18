# urls.py
from django.urls import path,include
from .views import RegistrationAPIView, LoginAPIView, UserApiView,CustomUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('usersapi/', UserApiView.as_view(), name='user'),
    path('', include(router.urls)),
]
