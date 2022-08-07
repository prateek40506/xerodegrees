from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'table', 'user_profile', 'order_total', 'status', 'placed_at')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'user_profile', 'table', 'menu_item', 'size', 'add_ons', 'quantity', 'placed_at')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)