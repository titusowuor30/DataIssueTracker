from rest_framework import serializers
from rest_framework.authtoken.models import Token
from DQIT_Endpoint.models import EmailSetup
from .models import Roles
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
import re
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import EmailMessage
import threading
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    # Include the CountryFieldSerializerMixin to handle the 'country' field
    country = serializers.CharField(source='get_country_display')  # Convert the 'country' field to a string
    timezone = serializers.SerializerMethodField()  # Add a SerializerMethodField

    class Meta:
        model = User
        fields = ['role', 'first_name', 'last_name','username','password','email', 'phone','gender','fcm_token','organisation','facilities','address','country','state','zip','timezone']
        depth = 2

    # Define a method to serialize the timezone field
    def get_timezone(self, obj):
        return str(obj.timezone)


    def test_thread(selft):
        print("sending email...")

    def create(self, validated_data):
        user = User(
        email = validated_data['email'],
        password = validated_data['password'],
        gender = validated_data['gender'],
        profile_pic = validated_data['profile_pic'],
        phone = validated_data['phone'],
        address = validated_data['address'],
        fcm_token = validated_data['fcm_token']
        )
        role = validated_data['role'],
        facilities = validated_data['facilities']
        user.is_active = False
        try:
            role,created=Roles.objects.get_or_create(role_name=role)
            user.role=role
        except Exception as e:
            print(e)
        user.save()
        user.facilities.set(facilities)
        token,created=Token.objects.create(user=user)
        # Send confirmation email
        config = EmailSetup.objects.first()
        print(config)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        subject = 'Confirm your registration'
        message = render_to_string('DQITAuth/confirm_email.html', {
            'user': user,
            'uid': uid,
            'token': token,
        })
        try:
            print(config.email_password)
            print(user.email)
            backend = EmailBackend(host=config.email_host, port=config.email_port, username=config.from_email,
                                   password=config.email_password, use_tls=config.use_tls, fail_silently=config.fail_silently)
            myemail = EmailMessage(subject=subject, body=message,
                                   from_email=config.from_email, to=[user.email,], connection=backend)
            # schedule in a thread
            email_thread = threading.Thread(target=myemail.send)
            print("Starting email thread..")
            email_thread.start()
            print("Email sent!")
        except Exception as e:
            print("send mail error:{}".format(e))
        return user
