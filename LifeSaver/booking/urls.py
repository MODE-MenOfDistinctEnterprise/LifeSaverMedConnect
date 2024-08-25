from django.urls import path
from . import views

# Setup URLs
# File: booking/urls.py

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('list/', views.booking_list, name='booking_list'),
]

