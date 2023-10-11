# Generated by Django 4.2.5 on 2023-10-04 19:59

from django.db import migrations
from DQITAuth.models import CustomUser, Roles

def create_initial_users(apps, schema_editor):
    # Get the Roles model
    #Roles = apps.get_model('DQITAuth', 'Roles')

    # Create user roles if they don't exist
    admin_role, created = Roles.objects.get_or_create(role_name='Admin')
    # Create initial users
    a_data={
        'username':'admin',
        'email':'admin@example.com',
        'first_name':'admin',
        'role':admin_role,  # Assign the Admin role
        'gender':'Male',
        'address':'Admin Address',
        'is_staff':True,
        'is_superuser':True
    }
    a,created=CustomUser.objects.get_or_create(
         email='admin@example.com',  # Use the email as the unique identifier
         defaults=a_data  # Provide the data to set if the user is created
    )
    a.set_password('@Admin123')
    a.save()

class Migration(migrations.Migration):
    dependencies = [
        ('DQITAuth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_users),
    ]
