# Generated by Django 4.2.5 on 2023-10-05 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DQIT_Endpoint', '0004_facilities_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataqualityissues',
            name='date_of_entry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datasyncsettings',
            name='faclity_list_csv_path',
            field=models.CharField(default='E:/projects/DataIssueTracker/DITApi/media/Hospital ID and Names.csv', max_length=500),
        ),
    ]