from django.shortcuts import render

from products.models import Product

# Create your views here.


def about(request):
    """ A view to return about us page with recommended products section"""   
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'about/about_us.html', context)       
