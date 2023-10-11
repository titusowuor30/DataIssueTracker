from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import Roles,PasswordPolicy,BackupSchedule


User=get_user_model()

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(User)
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
