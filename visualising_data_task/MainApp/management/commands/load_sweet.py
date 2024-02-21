from django.conf import settings
from django.core.management.base import BaseCommand
from MainApp.models import Sweet
import csv


class Command(BaseCommand):
    help = 'Populate the database with some data'

    def handle(self, *args, **kwargs):
        sweet_datafile = settings.BASE_DIR / 'data' / 'sweet_data.csv'

        with open(sweet_datafile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Sweet.objects.get_or_create(
                    name=row['sweet'],
                    mass=row['mass']
                )
