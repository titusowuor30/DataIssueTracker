# Generated by Django 4.2.5 on 2023-10-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DQITAuth', '0004_alter_backupschedule_db_backup_cmd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backupschedule',
            name='db_backup_cmd',
        ),
        migrations.AddField(
            model_name='backupschedule',
            name='db_type',
            field=models.CharField(choices=[('mysql', 'MySQL'), ('psql', 'PostgresSQL')], default='psql', max_length=10),
        ),
        migrations.AddField(
            model_name='backupschedule',
            name='restore_file',
            field=models.CharField(blank=True, default='E:\\projects\\DataIssueTracker\\DITApi\\media\x08ackups\x08ackup_2023_10_23_15-53-15.sql', max_length=255, null=True),
        ),
    ]
