from django.shortcuts import render, redirect, HttpResponse
from .models import Patient
from .forms import PatientForm


# Create your views here.
# views for patient management
# File: ehr/views.py

def index(request):
    return HttpResponse("Hello World!")

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect, HttpResponse('patient_list')
    else:
        form = PatientForm()
    return render(request, 'ehr/add_patient.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'ehr/patient_list.html', {'patients': patients})