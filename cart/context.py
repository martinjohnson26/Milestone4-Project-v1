from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

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
        'product_count': product_count,
        'postage': postage,
        'free_postage_delta': free_postage_delta,
        'free_postage_trigger': settings.FREE_POSTAGE_TRIGGER,
        'grand_total': grand_total,
    }

    return context