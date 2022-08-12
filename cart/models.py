from django.db import models
from table.models import Table
from foodmenu.models import MenuItem, AddOns, Size
from account.models import UserProfile
# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    addon = models.ForeignKey(AddOns, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def price(self):
        if self.size:
            if self.addon:
                return self.size.price + self.addon.price
            else:
                return self.size.price
        else:
            if self.addon:
                return self.menu_item.price + self.addon.price
            else:
                return self.menu_item.price

    def total_price(self):
        item_price = self.price()
        return self.quantity * item_price

    def __unicode__(self):
        return self.menu_item
