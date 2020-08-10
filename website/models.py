from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Costumer(models.Model):
    host_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    from_kakching = models.BooleanField()
    address = models.CharField(max_length=200)
    event = models.CharField(max_length=50)
    event_date = models.DateField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.host_name