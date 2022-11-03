import zoneinfo
from django.core.management.base import BaseCommand
import random
from farm_map.models import Produce, Farm_location, Position, Zone, Stack, User, Log_post

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('clearing farms')
        User.objects.exclude(is_superuser=True).delete()
        Farm_location.objects.all().delete()
        Produce.objects.all().delete()