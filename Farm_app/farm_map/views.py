from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Farm_location, Zone, Stack, Log_post, Calibration, Change_Log, User
import json 
from .forms import LoginForm, Harvest_forecast_form, LoginModelForm, Change_log_form, BuildFarm
from django.urls import reverse
from django.core.paginator import Paginator

from django.contrib import auth
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
app_name='farm_map'

def login(request):
    context = {
        'form': LoginForm(),
    }
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(request, username = username, password = password)
            
            if user != None:
                auth.login(request, user)
                
                
                return redirect('farm_map:index')

    return render(request, 'farm_map/login.html', context)


def index(request):
    context = {}
    
    if request.method == 'GET':
        if request.user.is_authenticated:
            user=request.user
            farms = Farm_location.objects.filter(user=user)
            for farm in farms:
                context['farm'] = farm 
                context['zones'] = [zone for zone in farm.zone.all()]
                print(context)
        else:
            dir_list = []
            for farm in Farm_location.objects.all():
                dir_list.append(farm.name)
            context['dir_list'] = dir_list

                    
        return render(request, 'farm_map/index.html', context)


@login_required(login_url='../login/')
def zone_view(request, zone_id):
    zone = Zone.objects.get(id=zone_id)
    context = {
        'zone': zone,
    }

    return render(request, 'farm_map/detail.html', context)


@login_required(login_url='../../login/')
def scout(request):
    if request.method == 'GET':
        return redirect('farm_map:index')
    if request.method == 'POST':
        data = json.loads(request.body)

        logtype = data.get('logtype', '')
        stack_id = data.get('stack_id', '')
        stack = Stack.objects.get(id=stack_id) 
        if logtype == 'Scout':
            stack.scout_week = (stack.scout_week+1)%5
            stack.scout_update = timezone.now()
            
            Log_post.objects.create(
                user = request.user,
                stack_id = stack_id,
                date = timezone.now()
            )
        elif logtype == 'Calibrate':
            stack.calibration_date = timezone.now()
            Calibration.objects.create(
                user = request.user,
                stack_id = stack_id,
                date = timezone.now()
            )
        stack.save()
        return JsonResponse({'response': 'logged'})

        
@login_required(login_url='../login/')
def logout(request):
    auth.logout(request)
    return redirect('farm_map:index')


@login_required(login_url='../login/')
def api_stack(request, stack_id):

        stack_list = []
        stack = Stack.objects.get(id=stack_id)
        stack_list.append({
            'id': stack.id,
            'identity' : stack.identity,
            'scout_week' : stack.scout_week,
            'scout_update' : stack.scout_update,
            'calibration_check' : stack.calibration_check,
            'calibration_date' : stack.calibration_date,
            'empty' : stack.empty,
            'to_harvest': stack.to_harvest(),
            'harvest_week': stack.harvest_week(),
            'to_calibrate': stack.to_calibrate(),


        })
        return JsonResponse(list(stack_list), safe=False)


@login_required(login_url='../../login/')
def harvest(request):
    if request.method == 'GET':
        return redirect('farm_map:index')
    if request.method == "POST":
        data = json.loads(request.body)
        stack_id = data.get('stack_id', '')
        stack = Stack.objects.get(id = stack_id)
        stack.empty = True
        stack.plant_date = None
        stack.scout_week = None
        stack.light_set_schedule = 2
        stack.save()
        
        return JsonResponse({'response' : 'harvested'})


@login_required(login_url='../../login/')
def plant(request):
    if request.method == 'GET':
        return redirect('farm_map:index')
    if request.method == "POST":
        data = json.loads(request.body)
        stack_id = data.get('stack_id', '')
        stack = Stack.objects.get(id = stack_id)
        stack.empty = False
        stack.plant_date = datetime.date.today()
        stack.scout_week = 0
        stack.save()

        return JsonResponse({'response' : 'planted'})

@login_required(login_url='../login/')
def light_schedule(request):
    # Update light state
    context = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        stack_id = data.get('stack_id', '')
        stack = Stack.objects.get(id = stack_id)
        if data.get('type') == 'switch':
            # Update light on/off
            stack.light_on = not stack.light_on
            stack.save()
            return JsonResponse({
                'response': 'switch',
                'light_state': stack.light_on, 
                'stack_id':stack.id,
                'empty': stack.empty,
            })
        # Update light schedule if necessary
        elif data.get('type') == 'change':
            stack.light_set_schedule = 2
            stack.save()
            return JsonResponse({
                'response': 'changed',
                'light_state': stack.light_on, 
                'stack_id':stack.id,
                'empty': stack.empty,
            })
        
        print(stack)
        

    if request.method == 'GET':
        if request.user.is_authenticated:
            user=request.user
            farms = Farm_location.objects.filter(user=user)
            for farm in farms:
                context['farm'] = farm
                context['zones'] = [zone for zone in farm.zone.all()]
                # Output Checking
                # for zone in farm.zone.all():
                #     for stack in zone.stack.all():
                #         print(stack.light_schedule())

    return render(request, 'farm_map/lights.html', context)


@login_required(login_url='../login/')
def task_viewer(request):
    context = {}

    if request.method == 'GET':

        farms = Farm_location.objects.filter(user=request.user)
        for farm in farms:
            context['farm'] = farm
            context['zones'] = [zone for zone in farm.zone.all()]
            

        return render(request, 'farm_map/task.html', context)

# TODO: Harvest forecast formula implementation
@login_required(login_url='../login/')
def harvest_forecast(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            context = { 'form': Harvest_forecast_form}

    

            return render(request, 'farm_map/forecast.html', context) 

@login_required(login_url='../login/')
def changelog(request):
    context = {}
    if request.user.is_authenticated:
        context['form'] = Change_log_form()
        change_logs = Change_Log.objects.exclude(restricted=True)
        context['change_logs'] = change_logs
        
    if request.method == 'POST':
        form=Change_log_form(request.POST)
        if form.is_valid():
            new_change = Change_Log.objects.create(
            suggestion = form.cleaned_data['suggestion'],
            restricted = form.cleaned_data['restricted'],
            user = request.user,
            farm = request.user.farm_location)
        return redirect(reverse('farm_map:changes'))

    return render(request, 'farm_map/changes.html', context)
                
def register(request):
    context=dict()
    context['form'] = BuildFarm()
    if request.method == "GET":
        context['form'] = BuildFarm()
    if request.method =='POST':
        form = BuildFarm(request.POST)
        if form.is_valid():
            print(form)
            # farm = Farm_location.objects.create(
            #     name=form.cleaned_data['farm_name']
            # )
            for zone in range(int(form.cleaned_data['zones'])):
                print(zone)

    
    return render(request, 'farm_map/register.html', context)