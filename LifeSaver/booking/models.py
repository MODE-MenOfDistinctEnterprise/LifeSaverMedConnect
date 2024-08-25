from django.db import models
from ehr.models import Patient

# Define the Booking model
# File: booking/models.py

# Create your models here.
class Booking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=255)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.patient.name} - {self.appointment_date} {self.appointment_time}"
