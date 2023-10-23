from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import Roles,PasswordPolicy,BackupSchedule
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password


User=get_user_model()

# Register the CustomUser model with the CustomUserAdmin class
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'role', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('role', 'gender', 'profile_pic', 'phone', 'address', 'organisation', 'country', 'state', 'zip', 'timezone', 'facilities', 'fcm_token')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role', 'gender', 'profile_pic', 'phone', 'address', 'organisation', 'country', 'state', 'zip', 'timezone', 'facilities', 'fcm_token')}
        ),
    )

admin.site.register(User,CustomUserAdmin)
# Register the Roles model
admin.site.register(Roles)


class BackupScheduleAdmin(admin.ModelAdmin):
    list_display = ('task_type', 'schedule_type', 'start_datetime', 'next_run_datetime', 'enabled')
    list_filter = ('task_type', 'schedule_type', 'enabled')
    search_fields = ('task_type', 'schedule_type', 'destination_path', 'source_path')

# Register the BackupSchedule model with the admin site
admin.site.register(BackupSchedule, BackupScheduleAdmin)

@admin.register(PasswordPolicy)
class PasswordPolicyAdmin(admin.ModelAdmin):
    list_display = ['min_length', 'min_uppercase_letters', 'min_lowercase_letters', 'min_digits', 'min_special_characters']
    list_editable = ['min_uppercase_letters', 'min_lowercase_letters', 'min_digits', 'min_special_characters']
    list_display_links = ['min_length']  # Choose a field for editing links
