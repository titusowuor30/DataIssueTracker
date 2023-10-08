from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from DQIT_Endpoint.models import Facilities

mobile_num_regex = RegexValidator(
        regex=r"^(?:\+254|0)[17]\d{8}$", message="Entered mobile number isn't in a right format!"
    )

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    GENDER = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    username = models.CharField(max_length=150, unique=True,blank=True,null=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey("Roles",on_delete=models.CASCADE,related_name='roles')
    gender = models.CharField(max_length=10, choices=GENDER)
    profile_pic = models.ImageField(upload_to='profiles',blank=True,null=True)
    address = models.TextField()
    facilities_assigned=models.ManyToManyField(Facilities,null=True,blank=True)
    fcm_token = models.TextField(default="")  # For firebase notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.email.split('@')[0])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Roles(models.Model):
    role_name=models.CharField(max_length=100)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table='Roles'
        managed=True
        verbose_name_plural='Roles'

