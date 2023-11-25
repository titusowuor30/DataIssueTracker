from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import (
    Roles,PasswordPolicy,BackupSchedule,
    AccountRequest,CustomUser,UserLog)
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password


User=get_user_model()

# Register the CustomUser model with the CustomUserAdmin class
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username','is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ( 'gender', 'pic', 'phone', 'address', 'organisation')}),
        ('Permissions', {'fields': ('user_permissions','groups','is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'gender', 'pic', 'phone', 'address', 'organisation', 'country', 'state', 'zip', 'timezone', 'facilities', 'fcm_token')}
        ),
    )

    #filter by facilities assigned if role not superuser
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Check if the user is a superuser
        if request.user.is_superuser:
            return qs  # Superusers can see all facilities

        # Filter the queryset to only show facilities assigned to the user
        return qs.filter(facilities__in=request.user.facilities.all())

admin.site.register(CustomUser,CustomUserAdmin)
# Register the Roles model
admin.site.register(Roles)

class UserLogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'timestamp', 'action')
    list_filter = ('id', 'user', 'timestamp', 'action')
    search_fields = ('id', 'user', 'timestamp', 'action')

# Register the BackupSchedule model with the admin site
admin.site.register(UserLog, UserLogsAdmin)

class BackupScheduleAdmin(admin.ModelAdmin):
    list_display = ('task_type', 'schedule_type', 'start_datetime', 'next_run_datetime', 'enabled')
    list_filter = ('task_type', 'schedule_type', 'enabled')
    search_fields = ('task_type', 'schedule_type', 'destination_path', 'source_path')

# Register the BackupSchedule model with the admin site
admin.site.register(BackupSchedule, BackupScheduleAdmin)

class AccountRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'request_date', 'is_approved')
    list_filter = ('email', 'username', 'request_date', 'is_approved')
    search_fields = ('email', 'username', 'request_date', 'is_approved')

# Register the BackupSchedule model with the admin site
admin.site.register(AccountRequest, AccountRequestAdmin)

@admin.register(PasswordPolicy)
class PasswordPolicyAdmin(admin.ModelAdmin):
    list_display = ['min_length', 'min_uppercase_letters', 'min_lowercase_letters', 'min_digits', 'min_special_characters']
    list_editable = ['min_uppercase_letters', 'min_lowercase_letters', 'min_digits', 'min_special_characters']
    list_display_links = ['min_length']  # Choose a field for editing links
