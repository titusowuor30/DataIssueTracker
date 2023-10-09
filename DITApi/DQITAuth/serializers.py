# serializers.py
from rest_framework import serializers
from .models import Roles
from django.contrib.auth import get_user_model

User=get_user_model()

# serializers.py
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name','phone','email', 'role', 'gender', 'profile_pic', 'address']

