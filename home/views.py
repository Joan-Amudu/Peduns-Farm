from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def privacy(request):
    """ A view to return the privacy policy """

    return render(request, 'privacy/privacy.html')


def accessability(request):
    """ A view to return the accessability statement """

    return render(request, 'accessability/accessability.html')
