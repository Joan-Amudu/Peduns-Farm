from django.shortcuts import render

from products.models import Product

# Create your views here.


def about(request):
    """ 
    A view to return about us page with recommended products section
    limit to only 4 products
    """   
    products = Product.objects.all()[0:4] 

    context = {
        'products': products,
    }

    return render(request, 'about/about_us.html', context)       
