# Generated by Django 4.2.5 on 2023-10-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DQITAuth', '0003_rename_mysql_cmd_path_backupschedule_db_backup_cmd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backupschedule',
            name='db_backup_cmd',
            field=models.CharField(default='mysqldump', help_text='Command for db backup', max_length=255),
        ),
    ]