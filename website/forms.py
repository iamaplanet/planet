from django import forms
from .models import Costumer, Invitee, Invitation

class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = ['application_number', 'host_name', 'mobile_number', 'email', 'from_kakching', 'address', 'event', 'event_date']

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['host', 'invitation']


class InviteeForm(forms.ModelForm):
    class Meta:
        model = Invitee
        fields = ['host', 'name', 'mobile_no', 'address']