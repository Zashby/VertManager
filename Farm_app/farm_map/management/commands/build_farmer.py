import zoneinfo
from django.core.management.base import BaseCommand
import random
from farm_map.models import Produce, Farm_location, Position, Zone, Stack, User, Log_post, Calibration
import datetime




class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        produce_3 = Produce.objects.create(
            type= 'Whole Head Lettuce',
            light_schedule_1 = 13.0,
            light_schedule_2 = 10.0,
            light_change = True,
            change_day = 14,
            harvest_time = 28
        )
        produce_4 = Produce.objects.create(
            type= 'Loose Leaf Lettuce',
            light_schedule_1 = 13.5,
            harvest_time = 21
        )
        farm = Farm_location.objects.create(
            name = 'FancierFarms'
        )
 
        users = []
        print('farm created')
        for x in range(21,30):
            print(f'creating user{x}')
            user = User.objects.create(
                username=f'user{x}',
                password='password',
                farm_location=farm

            )
            users.append(user)

        for x in range(1,4):
            print(f'zone{x}')
            zone = Zone.objects.create(
                identity = x,
                produce = produce_3,
                farm = farm
            )
            for y in range(1,10):
                print(f'zone{x} stack {y}')
                week_seed = random.randint(1,3)
                stack = Stack.objects.create(
                    zone = zone,
                    identity = y,
                    scout_week= week_seed,
                    scout_update = datetime.datetime.today() + datetime.timedelta(days = -29 + (7*week_seed)),
                    plant_date = datetime.datetime.today() + datetime.timedelta(days=-29)
                )
                if y%2 ==0:
                    calibration_seed = random.randint(-35,-15)
                    stack.calibration_date = datetime.datetime.today() + datetime.timedelta(days=calibration_seed)
                    stack.calibration_check = True
                    stack.save()
                    Calibration.objects.create(user = User.objects.get(
                    id = random.choice(users).id),
                    stack = stack,
                    date = datetime.datetime.today() + datetime.timedelta(days=calibration_seed )
                    )
                Log_post.objects.create(
                    user = User.objects.get(id = random.choice(users).id),
                    stack = stack,
                    date = datetime.datetime.today() + datetime.timedelta(days=random.randint(-14, 0))
                )
        for x in range(4,7):
            print(f'zone{x}')
            zone = Zone.objects.create(
                identity = x,
                produce = produce_4,
                farm = farm
            )
            for y in range(1,10):
                print(f'zone{x} stack {y}')
                week_seed = random.randint(1,3)
                stack = Stack.objects.create(
                    zone = zone,
                    identity = y,
                    scout_week= week_seed,
                    scout_update = datetime.datetime.today() + datetime.timedelta(days = -22 + (7*week_seed)),
                    plant_date = datetime.datetime.today() + datetime.timedelta(days=-22)
                    
                )
                if y%2 ==0:
                    calibration_seed = random.randint(-35,-15)
                    stack.calibration_date = datetime.datetime.today() + datetime.timedelta(days=calibration_seed)
                    stack.calibration_check = True
                    stack.save()
                    Calibration.objects.create(
                    user = User.objects.get(id = random.choice(users).id),
                    stack = stack,
                    date = datetime.datetime.today() + datetime.timedelta(days=calibration_seed)
                    )
                Log_post.objects.create(
                    user = User.objects.get(id = random.choice(users).id),
                    stack = stack,
                    date = datetime.datetime.today() + datetime.timedelta(days=random.randint(-14, 0))
                )