from django.shortcuts import render

# Create your views here.


def booking(request):
    """User fruit picking bookings"""

    if request.method == 'POST':        
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],            
            'date': request.POST['date'],
        }    

    template = 'bookings/booking.html'
    context = {}

    return render(request, template, context)
   