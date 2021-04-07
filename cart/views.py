from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """ Returns the shopping cart page """

    return render(request, 'cart/cart.html')
