from .models import Cart, CartItem
from .views import _cart_id


def total_cart_items(request):
    total = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()
    cart_items = CartItem.objects.filter(cart=cart)
    for cart_item in cart_items:
        total += cart_item.quantity
    return dict(total_cart_items=total)
