from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

import datetime
import time

class Species(models.Model):
    name = models.CharField(max_length=50)
    #Specifics regarding plant (nutrient requirements, alkalinity, etc.)
    # Maybe a link to an external website regarding plant
    def __str__(self):
        return self.name

class Produce(models.Model):
    type = models.CharField(max_length=25)
    species= models.ForeignKey(Species, related_name='species', blank=True, null=True, on_delete=models.PROTECT)
    light_change = models.BooleanField(default=False)
    change_day = models.IntegerField(blank = True, null = True)
    light_schedule_1 = models.FloatField(blank=True,)
    light_schedule_2 = models.FloatField(blank=True, null=True)
    harvest_time = models.IntegerField()
    
    def __str__(self):
        return self.type


class Farm_location(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Position(models.Model):

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Zone(models.Model):
    identity = models.IntegerField()
    produce = models.ForeignKey(Produce, related_name='zone', null=True, blank=True, on_delete=models.SET_NULL)
    farm = models.ForeignKey(Farm_location, related_name='zone', blank = True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Zone-{self.identity}'



class Stack(models.Model):
    scout_choices = [
        (1, 'first'),
        (2, 'second'),
        (3, 'third'),
        (4, 'fourth')
        ]

    light_choices=[
        (1, 'first'),
        (2, 'second')
    ]
    zone = models.ForeignKey(Zone, related_name='stack', null=True, blank=True, on_delete=models.CASCADE)
    identity = models.IntegerField()
    scout_week = models.IntegerField(choices= scout_choices, blank=True, null=True)
    scout_update = models.DateField(blank=True, null=True)
    calibration_check = models.BooleanField(default=False)
    calibration_date = models.DateField(blank=True, null=True)
    empty = models.BooleanField(default=False)
    plant_date = models.DateField(blank=True, null=True, default=datetime.datetime.now)
    light_on = models.BooleanField(default=False)
    automatic_lights = models.BooleanField(default=False)
    light_set_schedule = models.IntegerField(choices= light_choices, default=1)

    def __str__(self):
        return f'{self.zone}-{self.identity}'

    def maintained(self):
        if self.calibration_check == True and self.empty == False:
            return (self.log_post.all().last().to_scout()) and (self.calibration.all().last().to_calibrate())
        else:
            return self.log_post.all().last().to_scout()
        
    def to_harvest(self):
        if self.empty == False:
            return ( datetime.date.today() > self.plant_date + datetime.timedelta(self.zone.produce.harvest_time))
    
    def harvest_date(self):
        if self.empty == False:
            return self.plant_date + datetime.timedelta(self.zone.produce.harvest_time)

    def harvest_week(self):
        return self.zone.produce.harvest_time // 7

    def to_scout(self):
        if not self.empty and self.scout_week > 0:
            return datetime.datetime.today() > self.log_post.all().last().date + datetime.timedelta(days=7)
        else:
            return False

    def to_calibrate(self):
        if self.calibration_check:
            return datetime.date.today() > self.calibration_date + datetime.timedelta(days=30)
        else:
            return False

    def light_change(self):
        if not self.empty:
            if self.light_set_schedule == 1:
                if self.zone.produce.light_change:
                    return self.plant_date + datetime.timedelta(days=self.zone.produce.change_day) <= datetime.date.today()
            else:
                return False

    def light_schedule(self):
        if self.automatic_lights:
            time.localtime()
            if not self.light_change():
                return datetime.datetime.now().hour
            if self.light_change():
                return datetime.datetime.now().hour + datetime.timedelta(hours = 6)
        else:
            return datetime.datetime.now().hour 

class User(AbstractUser):
    position = models.ManyToManyField(Position, related_name='user', blank=True)
    farm_location = models.ForeignKey(Farm_location, blank=True, null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return self.username


class Log_post(models.Model):

    user = models.ForeignKey(User, related_name='scouter', on_delete=models.CASCADE)
    stack = models.ForeignKey(Stack, related_name='log_post', on_delete=models.CASCADE)
    date = models.DateTimeField(default= datetime.datetime.now)

    def __str__(self):
        return f'{self.stack} | {self.user} | {self.date.strftime("%Y-%m-%d %H:%M:%S %Z")}'

    def log(self):
        return f'{self.user} | {self.date.strftime("%Y-%m-%d %H:%M:%S %Z")}'

    def to_scout(self):
        return datetime.datetime.today() < self.date + datetime.timedelta(days=7)


class Calibration(models.Model):

    user = models.ForeignKey(User, related_name='calibrator', on_delete=models.CASCADE)
    stack = models.ForeignKey(Stack, related_name='calibration', on_delete=models.CASCADE)
    date = models.DateTimeField(default= datetime.datetime.now)

    def __str__(self):
        return f'{self.stack} | {self.user} | {self.date.strftime("%Y-%m-%d %H:%M:%S %Z")}'

    def log(self):
        return f'{self.user} | {self.date.strftime("%Y-%m-%d %H:%M:%S %Z")}'

    def to_calibrate(self):
        return datetime.datetime.today() < self.date + datetime.timedelta(30)


class Harvest_Forecast(models.Model):
    user = models.ForeignKey(User, related_name='forecaster', on_delete = models.CASCADE)
    stack = models.ForeignKey(Stack, related_name='harvest_forecast', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    percentage = models.FloatField(blank=True, null=True)
    dry_weight = models.FloatField(null=True)

class Change_Log(models.Model):
    user=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm_location, related_name='farm', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True, blank=True, null=True)
    suggestion = models.TextField(max_length=255)
    restricted = models.BooleanField(default=True)
    immolate = models.BooleanField(default=False)
    Working = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    votes = models.ManyToManyField(User, related_name='voter')
    down_votes = models.ManyToManyField(User, related_name='down_voter')

    def voted(self):
        return(len(self.votes))

    def downVote(self):
        return (len(self.down_vote))
