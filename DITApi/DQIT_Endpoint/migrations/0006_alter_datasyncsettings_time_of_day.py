# Generated by Django 4.2.5 on 2023-10-23 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DQIT_Endpoint', '0005_alter_datasyncsettings_time_of_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasyncsettings',
            name='time_of_day',
            field=models.TimeField(default=datetime.time(13, 18, 16, 489765)),
        ),
    ]
