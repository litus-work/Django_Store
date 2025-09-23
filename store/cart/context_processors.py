from .cart import Cart

def cart(request):
    c = Cart(request)
    return {
        'cart': c,
        'cart_count': len(c),
        'cart_total': c.get_total_price(),
    }
