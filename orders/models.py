from django.db import models
from table.models import Table
from account.models import UserProfile
from cart.models import Cart, CartItem
from foodmenu.models import MenuItem, AddOns, Size


# Create your models here.
class Order(models.Model):
    choices = (
        ('placed', 'placed'),
        ('delivered', 'delivered')
    )
    order_id = models.CharField(max_length=20)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order_note = models.CharField(max_length=100, blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=50, choices=choices, default='placed')
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    add_ons = models.ForeignKey(AddOns, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.menu_item.item_name







