"""
URL configuration for LifeSaver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from ehr.views import index
from ehr.views import add_patient
from ehr.views import patient_list
from booking.views import book_appointment
from booking.views import booking_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ehr/', include('ehr.urls')),
    path('booking/', include('booking.urls')),
    path('', index),
    path('add/', add_patient),
    path('list/', patient_list),
    path('book/', book_appointment),
    path('list/', booking_list),
]

