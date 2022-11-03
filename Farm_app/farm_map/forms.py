from django import forms
from .models import User, Zone, Stack, Harvest_Forecast, Change_Log


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12, label='username')
    password = forms.CharField(max_length=12, label='password' , widget=forms.PasswordInput, )

class LoginModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class Harvest_forecast_form(forms.ModelForm):

    class Meta:
         model = Harvest_Forecast
         fields = ['stack', 'dry_weight']

class Change_log_form(forms.ModelForm):

    class Meta:
        model= Change_Log
        fields = ['restricted','suggestion' ]