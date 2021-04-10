from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from programmes.models import Programme


def cart_contents(request):

    cart_items = []
    total = 0
    programme_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        programme = get_object_or_404(Programme, pk=item_id)
        total += quantity * programme.price
        programme_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'programme': programme,
        })

    if total < settings.FREE_POSTAGE_TRIGGER:
        postage = total * Decimal(settings.STANDARD_POSTAGE_PERCENTAGE / 100)
        free_postage_delta = settings.FREE_POSTAGE_TRIGGER - total
    else:
        postage = 0
        free_postage_delta = 0

    grand_total = postage + total


    context = {
        'cart_items': cart_items,
        'total': total,
        'programme_count': programme_count,
        'postage': postage,
        'free_postage_delta': free_postage_delta,
        'free_postage_trigger': settings.FREE_POSTAGE_TRIGGER,
        'grand_total': grand_total,
    }

    return context