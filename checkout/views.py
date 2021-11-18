from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your shopping cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jk1qhFzc3HPKNytHVQMa12GfU7kPLzUaU0kL12wWt9Vr61GWRyYFOUQ0AyXYTw1l5dj40LGC94rchh2AlkBeSeu00avOGTE74',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)