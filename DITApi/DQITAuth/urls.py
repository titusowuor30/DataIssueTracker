# urls.py
from django.urls import path,include
from .views import RegistrationAPIView, LoginAPIView, UserAPIView,CustomUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/', UserAPIView.as_view(), name='user'),
    path('', include(router.urls)),
]
