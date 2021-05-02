from django.core.management.base import BaseCommand

from ...models import User

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        username = 'admin'
        password = '12345678'
        try:
            admin_user = User.objects.get(username=username)
            print(f'Admin user {admin_user.username} with password {password} exists...')
        except User.DoesNotExist:
            user = User.objects.create_superuser(username, password)
            print(f'Created admin user {user} with password {password}')