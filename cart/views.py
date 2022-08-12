from django.shortcuts import render, redirect
from .models import Cart, CartItem
from foodmenu.models import MenuItem, Size, AddOns


def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

# Create your views here.


def cart(request):
    total = 0
    quantity = 0
    tax = 0
    grand_total = 0
    cart_items = CartItem.objects.filter(cart__cart_id=_cart_id(request), is_active=True)
    if cart_items is not None:
        for cart_item in cart_items:
            total += cart_item.total_price()
            quantity += cart_item.quantity
        tax = (2 * total) / 100
        grand_total += total + tax
    context = {
        'cart_items': cart_items,
        'quantity': quantity,
        'total': total,
        'tax': tax,
        'grand_total': grand_total
    }
    return render(request, 'cart.html', context)


def add_cart(request, menu_item_id=None):
    if request.method == 'POST':
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id=_cart_id(request)
            )
            cart.save()
        item = MenuItem.objects.get(id=menu_item_id)
        size = None
        add_on = None
        if item.is_size():
            item_size = request.POST['size']
            size = Size.objects.get(menu_item=item, size=item_size)
        addon = request.POST['addon']
        variation = request.POST['variation']
        if addon != "":
            if variation != "":
                add_on = AddOns.objects.get(menu_item=item, add_ons=addon, variation=variation)
        try:
            cart_item = CartItem.objects.get(menu_item=item, size=size, addon=add_on, cart=cart)
            cart_item.quantity += 1
        except CartItem.DoesNotExist:
            cart_item = CartItem(
                menu_item=item,
                size=size,
                addon=add_on,
                cart=cart,
                quantity=1
            )
        cart_item.save()
        return redirect('cart')


def increment_qty(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def decrement_qty(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def delete_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart')









