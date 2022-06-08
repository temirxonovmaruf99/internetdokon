from django.conf import settings as django_settings


def add_cart(request):
    cart = request.session.get('cart')
    return {
        'cart': cart,
        'cart_n': sum(cart.values()) if cart is not None else 0
    }



