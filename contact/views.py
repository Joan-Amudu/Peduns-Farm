from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    """ A view to return the contact us page """

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'message': request.POST['message'],            
        }
    contact_form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
