from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Produce, Farm_location, Position, Zone, Stack, Log_post, Calibration, Change_Log, Species
# Register your models here.

admin.site.register(Produce)

admin.site.register(Farm_location)

admin.site.register(Position)

admin.site.register(Zone)

admin.site.register(Stack)

admin.site.register(Log_post)

admin.site.register(Calibration)

admin.site.register(Change_Log)

admin.site.register(Species)

class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('farm_location',)}),
    )

admin.site.register(User, MyUserAdmin)





