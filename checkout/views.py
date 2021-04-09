from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('programmes'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IeIuJLo2DoyD1o4qa8eRrxRxJ8ELT22rBObMY2Agsw9nBn4w5Kqq6ff1f5vz4ujapJ8zrBvyIMLnMTvmWcSv3ok00Kt8JyQUS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
