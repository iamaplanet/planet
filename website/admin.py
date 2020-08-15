from django.contrib import admin
from .models import Costumer, Invitation, Invitee

# Register your models here.
admin.site.register(Costumer)
admin.site.register(Invitation)
admin.site.register(Invitee)