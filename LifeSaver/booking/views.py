from django.shortcuts import render, redirect, HttpResponse
from .models import Booking
from .forms import BookingForm

# Create views for appointment management
# File: booking/views.py

# Create your views here.
def book_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect, HttpResponse('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/book_appointment.html', {'form': form})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})