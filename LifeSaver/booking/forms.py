from django import forms
from .models import Booking

# Create forms for Booking
# File: booking/forms.py

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['patient', 'doctor_name', 'appointment_date', 'appointment_time']