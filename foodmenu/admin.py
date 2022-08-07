from django.contrib import admin
from django.utils.html import format_html
from .models import MenuItem, AddOns, Size
# Register your models here.


class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('item_name',)
    }

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%;">'.format(obj.image.url))
        else:
            return format_html(
                '<img src="https://cdn1.vectorstock.com/i/1000x1000/50/20/no-photo-or-blank-image-icon-loading-images-vector-37375020.jpg" width="50" height="50" style="border-radius:50%;">')

    thumbnail.short_description = 'Item Image'
    list_display = ('item_name', 'slug', 'category', 'type', 'price', 'sales', 'thumbnail', 'is_available')


class AddOnsAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'add_ons', 'variation', 'price')


class SizeAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'size', 'price')


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(AddOns, AddOnsAdmin)
admin.site.register(Size, SizeAdmin)


