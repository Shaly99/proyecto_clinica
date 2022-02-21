from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Patient(models.Model):
    first_name = models.CharField(max_length= 250)
    last_name = models.CharField(max_length= 250)
    phone_number = models.CharField(max_length= 250)
    email = models.CharField(max_length= 250)
    address = models.CharField(max_length= 250)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    social_security_number = models.IntegerField()
    clinic_history_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.social_security_number}"