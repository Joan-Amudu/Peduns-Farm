from django.shortcuts import render

# Create your views here.


def booking(request):
    """User fruit picking bookings"""
    template = 'bookings/booking.html'
    context = {}

    return render(request, template, context)