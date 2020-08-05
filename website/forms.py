from django import forms
from .models import Costumer

class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = ['host_name', 'mobile_number', 'email', 'from_kakching', 'address', 'event', 'event_date', 'description']