from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import src.core.management.utils as utils


class Command(BaseCommand):
    help = 'Install all data'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin'
            )
            self.stdout.write(self.style.SUCCESS('Superuser was created.'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser has been created.'))

        utils.install_client(self)
        utils.install_product(self)
        utils.install_warehouse(self)
        utils.install_organization(self)
