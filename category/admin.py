from django.contrib import admin
from django.utils.html import format_html
from .models import Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('category_name',)
    }
    
    def thumbnail(self, obj):
        if obj.cat_image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;">'.format(obj.cat_image.url))
        else:
            return format_html('<img src="https://cdn1.vectorstock.com/i/1000x1000/50/20/no-photo-or-blank-image-icon-loading-images-vector-37375020.jpg" width="50" height="50" style="border-radius:50%;">')
    thumbnail.short_description = 'Category Image'
    list_display = ('category_name', 'slug', 'thumbnail')


admin.site.register(Category, CategoryAdmin)
