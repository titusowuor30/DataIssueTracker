from django.contrib import admin
from .models import DataQualityIssues, Facilities, EmailSetup, DataSyncSettings

@admin.register(DataQualityIssues)
class DataQualityIssuesAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'facility', 'date_of_entry', 'inconsistency', 'action_taken', 'date_action_taken')
    list_filter = ('facility', 'date_of_entry','action_taken', 'date_action_taken')
    search_fields = ('patient_id', 'facility', 'date_of_entry', 'inconsistency', 'action_taken', 'date_action_taken')

@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ('facility_code', 'facility_name','country')
    list_filter = ('country',)
    search_fields = ('facility_code', 'facility_name','country')

@admin.register(EmailSetup)
class EmailSetupAdmin(admin.ModelAdmin):
    list_display = ('support_reply_email_name', 'support_reply_email', 'email_password', 'email_port', 'email_backed', 'email_host', 'fail_silently', 'use_tls')
    list_filter = ('support_reply_email_name', 'support_reply_email', 'email_password', 'email_port', 'email_backed', 'email_host', 'fail_silently', 'use_tls')


@admin.register(DataSyncSettings)
class DataSyncSettingsAdmin(admin.ModelAdmin):
    list_display = ('data_issues_folder_url','faclity_list_csv_path','data_sync_frequency')
    list_filter= ('data_issues_folder_url','faclity_list_csv_path','data_sync_frequency')
    search_fields= ('data_issues_folder_url','faclity_list_csv_path','data_sync_frequency')
