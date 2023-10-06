from django.db import models
from tinymce.models import HTMLField

class DataQualityIssues(models.Model):
    ACTIONS=(
    ('Entry Corrected', 'Entry Corrected'),
    ('Data Matches Source Document', 'Data Matches Source Document'),
    ('Data Already Available', 'Data Already Available'),
    ('No Data Needed', 'No Data Needed'),
    ('Pending', 'Pending'),
    )
    patient_id = models.CharField(max_length=100)
    facility = models.ForeignKey('Facilities',on_delete=models.CASCADE,related_name='issues')
    date_of_entry = models.DateField(blank=True,null=True)
    inconsistency = HTMLField()
    action_taken = models.CharField(max_length=100,choices=ACTIONS,default='Pending')
    date_action_taken = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.facility.facility_code

    class Meta:
        db_table='data_issues'
        managed=True
        verbose_name_plural='Data Quality Issues'


class Facilities(models.Model):
    facility_code=models.CharField(max_length=100)
    facility_name=models.CharField(max_length=100)
    country=models.CharField(max_length=255,default='Kenya')

    def __str__(self):
        return self.facility_code +' '+self.facility_name

    class Meta:
        db_table='Faclities'
        managed=True
        verbose_name_plural='Facilities'


class EmailSetup(models.Model):
    support_reply_email_name = models.CharField(
        max_length=255, default='DQITs Center', blank=True, null=True)
    support_reply_email = models.EmailField(
        max_length=255, default='titusowuor30@gmail.com', blank=True, null=True)
    email_password = models.CharField(
        max_length=255, default='xdofqrtncuimlewm', blank=True, null=True)
    email_port = models.IntegerField(default=587, blank=True, null=True)
    email_backed = models.CharField(
        max_length=100, default='smtp', blank=True, null=True)
    email_host = models.CharField(
        max_length=255, default='smtp.gmail.com', blank=True, null=True)
    fail_silently = models.BooleanField(default=True, blank=True, null=True)
    use_tls = models.BooleanField(default=True, blank=True, null=True)
    code_place_holders = HTMLField(blank=True, null=True)


    def __str__(self):
        return self.support_reply_email_name

    class Meta:
        verbose_name_plural='Email Settings'


class DataSyncSettings(models.Model):
    data_issues_folder_url=models.CharField(max_length=500,default='E:/projects/DataIssueTracker/DITApi/media/facility data issues')
    faclity_list_csv_path=models.CharField(max_length=500,default='E:/projects/DataIssueTracker/DITApi/media/Hospital ID and Names.csv')
    data_sync_frequency=models.IntegerField(default=60,help_text='In seconds')
    data_sync_shedule_date=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.data_issues_folder_url

    class Meta:
        verbose_name_plural='Data Sync Settings'

