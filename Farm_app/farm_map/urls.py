from django.urls import path
from . import views

app_name='farm_map'

urlpatterns = [
    path('', views.index, name='index'),

    path('zoneview/<int:zone_id>', views.zone_view, name='zone_view'),

    path('zoneview/scout/', views.scout, name='scout'),

    path('logout/', views.logout, name='logout'),
    
    path('api/stack/<int:stack_id>', views.api_stack, name='api_stack'),

    path('api/farm_manage/<int:farm_id>', views.api_management, name='api_management'),

    path('login/', views.login, name='login'),

    path('zoneview/harvest/', views.harvest, name='harvest'),

    path('zoneview/plant/', views.plant, name='plant'),

    path('lights/', views.light_schedule, name='lights'),

    path('tasks/', views.task_viewer, name='task_viewer'),

    path('management/', views.management, name='management'),

    path('change/', views.changelog, name='changes'),

    path('register/', views.register, name='register'),
]