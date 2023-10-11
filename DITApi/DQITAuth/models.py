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
from django.utils import timezone
from django_countries.fields import CountryField
from timezone_field import TimeZoneField

mobile_num_regex = RegexValidator(
        regex=r"^(?:\+254|0)[17]\d{8}$", message="Entered mobile number isn't in a right format!"
    )

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
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.email.split('@')[0])
            self.password=self.set_password(self.password)
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

    task_type = models.CharField(max_length=10, choices=TASK_CHOICES, default='backup')
    schedule_type = models.CharField(max_length=10, choices=SCHEDULE_CHOICES, default='daily')
    start_datetime = models.DateTimeField(default=timezone.now)
    last_run_datetime = models.DateTimeField(null=True, blank=True)
    next_run_datetime = models.DateTimeField(null=True, blank=True)
    enabled = models.BooleanField(default=True)
    destination_path = models.CharField(max_length=255)
    source_path = models.CharField(max_length=255)

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


