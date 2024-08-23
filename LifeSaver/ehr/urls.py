from django.urls import path
from . import views

# Setup URLs
# File: ehr/urls.py

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('list/', views.patient_list, name='patient_list'),
]