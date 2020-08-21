from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Costumer(models.Model):
    application_number = models.CharField(max_length=50)
    host_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    from_kakching = models.BooleanField()
    address = models.CharField(max_length=200)
    event = models.CharField(max_length=50)
    event_date = models.DateField()

    def __str__(self):
        return self.application_number

class Invitation(models.Model):
    host = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    invitation = models.CharField(max_length=50)

    def __str__(self):
        return self.invitation


class Invitee(models.Model):
    host = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name