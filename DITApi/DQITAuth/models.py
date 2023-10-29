from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import (AbstractUser,BaseUserManager)
from django.utils.text import slugify
from DQIT_Endpoint.models import Facilities
from django.utils import timezone
from django_countries.fields import CountryField
from timezone_field import TimeZoneField
from tinymce.models import HTMLField

mobile_num_regex = RegexValidator(
        regex=r"^(?:\+254|0)[17]\d{8}$", message="Entered mobile number isn't in a right format!"
    )

class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone, password='@User123', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    GENDER = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    username = models.CharField(max_length=150, unique=True,blank=True,null=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey("Roles",on_delete=models.CASCADE,related_name='roles')
    gender = models.CharField(max_length=10, choices=GENDER)
    profile_pic = models.ImageField(upload_to='profiles',blank=True,null=True)
    phone=models.CharField(max_length=15,default='+254743793901')
    address = models.TextField(blank=True,null=True)
    organisation=models.CharField(max_length=100,default='DQIts')
    country=CountryField(max_length=255,blank=True,null=True)
    state=models.CharField(max_length=255,default='Kenya',blank=True,null=True)
    zip=models.CharField(max_length=10,default='00100',blank=True,null=True)
    timezone=TimeZoneField(choices_display="WITH_GMT_OFFSET",use_pytz=True,default="Africa/Nairobi",blank=True,null=True)
    facilities=models.ManyToManyField(Facilities,null=True,blank=True)
    fcm_token = models.TextField(default="None")  # For firebase notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ip_address=models.CharField(max_length=100,default="192.168.0.1")
    device=models.CharField(max_length=100,default="Phone")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects=CustomUserManager()


    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.email.split('@')[0])
            self.password=make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name

class PasswordPolicy(models.Model):
    MIN_LENGTH_CHOICES = (
        (6, '6 characters'),
        (8, '8 characters'),
        (10, '10 characters'),
        (16, '16 characters'),
        # Add more choices as needed
    )

    MIN_UPPERCASE_LETTERS_CHOICES = (
        (1, 'At least 1 uppercase letter'),
        (2, 'At least 2 uppercase letters'),
        # Add more choices as needed
    )

    MIN_LOWERCASE_LETTERS_CHOICES = (
        (1, 'At least 1 lowercase letter'),
        (2, 'At least 2 lowercase letters'),
        # Add more choices as needed
    )

    MIN_DIGITS_CHOICES = (
        (1, 'At least 1 digit'),
        (2, 'At least 2 digits'),
        # Add more choices as needed
    )

    MIN_SPECIAL_CHARACTERS_CHOICES = (
        (0, 'None'),
        (1, 'At least 1 special character'),
        (2, 'At least 2 special characters'),
        # Add more choices as needed
    )

    min_length = models.IntegerField(choices=MIN_LENGTH_CHOICES, default=8)
    min_uppercase_letters = models.IntegerField(choices=MIN_UPPERCASE_LETTERS_CHOICES, default=1)
    min_lowercase_letters = models.IntegerField(choices=MIN_LOWERCASE_LETTERS_CHOICES, default=1)
    min_digits = models.IntegerField(choices=MIN_DIGITS_CHOICES, default=1)
    min_special_characters = models.IntegerField(choices=MIN_SPECIAL_CHARACTERS_CHOICES, default=0)

    def __str__(self):
        return "Password Policy"
    class Meta:
        verbose_name_plural='Password Policy'

class BackupSchedule(models.Model):
    SCHEDULE_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    TASK_CHOICES = [
        ('backup', 'Backup'),
        ('restore', 'Restore'),
    ]

    DB_CHOICES = [
        ('mysql', 'MySQL'),
        ('psql', 'PostgresSQL'),
    ]

    task_type = models.CharField(max_length=10, choices=TASK_CHOICES, default='backup')
    db_type = models.CharField(max_length=10, choices=DB_CHOICES, default='psql')
    schedule_type = models.CharField(max_length=10, choices=SCHEDULE_CHOICES, default='daily')
    start_datetime = models.DateTimeField(default=timezone.now)
    last_run_datetime = models.DateTimeField(null=True, blank=True)
    next_run_datetime = models.DateTimeField(null=True, blank=True)
    enabled = models.BooleanField(default=True)
    folder_path = models.CharField(max_length=255,default='E:\projects\DataIssueTracker\DITApi\backups',help_text="Backup folder path")
    restore_file=models.CharField(max_length=255,blank=True,null=True,default='E:\projects\DataIssueTracker\DITApi\backups\backup_2023_10_23_15-53-15.sql',help_text="Restore file path")

    def __str__(self):
        return f'{self.get_task_type_display()} Schedule ({self.get_schedule_type_display()})'

    def save(self, *args, **kwargs):
        # Calculate the next run datetime based on the schedule_type and start_datetime
        if self.schedule_type == 'daily':
            self.next_run_datetime = self.start_datetime + timezone.timedelta(days=1)
        elif self.schedule_type == 'weekly':
            self.next_run_datetime = self.start_datetime + timezone.timedelta(weeks=1)
        elif self.schedule_type == 'monthly':
            self.next_run_datetime = self.start_datetime + timezone.timedelta(days=30)  # Approximate for a month

        super().save(*args, **kwargs)


class Roles(models.Model):
    role_name=models.CharField(max_length=100)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table='Roles'
        managed=True
        verbose_name_plural='Roles'


class AccountRequest(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    account_information=HTMLField()
    request_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class UserLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - { self.action}"