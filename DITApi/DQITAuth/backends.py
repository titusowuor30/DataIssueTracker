from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import PasswordPolicy

class PasswordPolicyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None

    def validate_password(self, password):
        policy = PasswordPolicy.objects.first()

        if len(password) < policy.min_length:
            raise ValidationError(f"Password must be at least {policy.min_length} characters long.")

        if sum(c.isupper() for c in password) < policy.min_uppercase_letters:
            raise ValidationError(f"Password must contain at least {policy.min_uppercase_letters} uppercase letter(s).")

        if sum(c.islower() for c in password) < policy.min_lowercase_letters:
            raise ValidationError(f"Password must contain at least {policy.min_lowercase_letters} lowercase letter(s).")

        if sum(c.isdigit() for c in password) < policy.min_digits:
            raise ValidationError(f"Password must contain at least {policy.min_digits} digit(s).")

        special_characters = "!@#$%^&*()-_+=[]{}|;:'\",.<>?/\\"
        if sum(c in special_characters for c in password) < policy.min_special_characters:
            raise ValidationError(f"Password must contain at least {policy.min_special_characters} special character(s).")

