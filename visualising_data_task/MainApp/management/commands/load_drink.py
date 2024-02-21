from django.conf import settings
from django.core.management.base import BaseCommand
from MainApp.models import Drink
import csv

class Command(BaseCommand):
    help = 'Populate the database with some data'

    def handle(self, *args, **kwargs):
        drink_datafile = settings.BASE_DIR / 'data' / 'drink_data.csv'

        with open(drink_datafile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Drink.objects.get_or_create(
                    name=row['drink'],
                    litre=row['litre']
                )

