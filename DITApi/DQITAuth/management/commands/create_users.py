# ../management/commands/create_users.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from DQITAuth.models import Roles  # Import your Role model
User=get_user_model()

class Command(BaseCommand):
    help = 'Create superuser or users with roles'

    def handle(self, *args, **options):
        # Create a superuser
        if not User.objects.filter(username='admin').exists():
            role,created= Roles.objects.get_or_create(role_name='Admin')  # Set the user's role
            admin = User.objects.create_superuser(username='admin',first_name='Titus',last_name='Owuor',password='@Admin123', email='titus.owuor@bengohub.co.ke',role=role)

        # Create users with roles
        if not User.objects.filter(username='user1').exists():
            role,created= Roles.objects.get_or_create(role_name='User')  # Set the user's role
            user1 = User.objects.create_user(email='user1@example.com', password='@User123',role=role,phone='+254743793901')

        self.stdout.write(self.style.SUCCESS('Users and roles created successfully'))
