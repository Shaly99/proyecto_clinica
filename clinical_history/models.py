from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from patient.models import Patient


class ClinicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinic_history_number = models.IntegerField()
    lab_result = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=250)
    vitals_signs = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.patient.__str__()} {self.clinic_history_number}'