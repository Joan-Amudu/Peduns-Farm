import random
from django.shortcuts import render
from products.models import Product

# Create your views here.


def about(request):
    """
    A view to return about us page with recommended products section
    Recommended Products are shuffled
    """

    products = list(Product.objects.all())
    random.shuffle(products)

    context = {
        'products': products,
    }

    return render(request, 'about/about_us.html', context)
