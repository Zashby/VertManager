

*Farm_location
    name
            *Zone:
                identity
                *produce:
                    type
                    light_schedule
                    harvest_time 
                farm
                *Stack:
                    
                    zone
                    identity 
                    scout_week
                        scout_choices = [
                        (1, 'first'),
                        (2, 'second'),
                        (3, 'third'),
                        (4, 'fourth')
                        ]
                    scout_update
                    calibration_check
                    calibration_date
                    empty


*User:
    *position:
        title
    farm_location


*Log_post:
    
    user
    stack
    log_type
        log_choices = [
        ('Scout','Scout'),
        ('Calibrate', 'Calibrate')
        ]
    date





def to_calibrate(self):
        return datetime.datetime.today() < self.date + datetime.timedelta(14)




plant_date = models.DateField(blank=True, auto_now_add=True)
 def harvest(self):
    #     return self.plant_date + datetime.timedelta(Zone.objects.get(id=self.zone).produce.harvest_time) >= datetime.datetime.today()
