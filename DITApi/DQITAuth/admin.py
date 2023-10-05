from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import Roles

User=get_user_model()

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(User)
# Register the Roles model
admin.site.register(Roles)