from .models import Cart, CartItems
from .views import _cart_id


def counter(request):
    cart_count = 0      # var coz counter number on  cart
    if 'admin' in request.path:            # request path if admin can you though data to return see anything
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItems.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_item = 0
    return dict(cart_count=cart_count)
