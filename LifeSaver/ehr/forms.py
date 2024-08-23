from django import forms
from .models import Patient

# Create forms for Patient
# File: ehr/forms.py

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'medical_history']