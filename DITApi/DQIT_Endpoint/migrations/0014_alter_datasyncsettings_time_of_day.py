# Generated by Django 4.2.5 on 2023-10-29 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DQIT_Endpoint', '0013_alter_datasyncsettings_time_of_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasyncsettings',
            name='time_of_day',
            field=models.TimeField(default=datetime.time(10, 12, 30, 344477)),
        ),
    ]
