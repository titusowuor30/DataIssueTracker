# Generated by Django 4.2.5 on 2023-10-05 18:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('DQIT_Endpoint', '0007_alter_dataqualityissues_action_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataqualityissues',
            name='inconsistency',
            field=tinymce.models.HTMLField(),
        ),
    ]