from django.shortcuts import render
from .forms import BookingForm
# Create your views here.


def booking(request):
    """User fruit picking bookings"""

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'number_of_people': request.POST['number_of_people'],
            'date': request.POST['date'],
        }
    booking_form = BookingForm()
    template = 'bookings/booking.html'
    context = {
        'booking_form': booking_form,
    }

    return render(request, template, context)
