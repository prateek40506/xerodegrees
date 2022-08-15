from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.


class MenuItem(models.Model):
    choices_type = (
        ('None', 'None'),
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg')
    )

    item_name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=100, choices=choices_type)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField(blank=True)
    sales = models.IntegerField(default=0)
    image = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)

    def is_size(self):
        if self.price in (0, 1):
            return True
        else:
            return False

    def get_url(self):
        return reverse('item_details', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.item_name


class AddOns(models.Model):
    choices = (
        ('Cheesy', 'Cheesy'),
        ('Peri Peri', 'Peri Peri'),
        ('Sauces', 'Sauces'),
        ('Flavours', 'Flavours')
    )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    add_ons = models.CharField(max_length=50, choices=choices)
    variation = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'addons'
        verbose_name_plural = 'add ons'

    def __str__(self):
        return self.add_ons


class Size(models.Model):
    choices = (
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Small', 'Small'),
        ('Regular', 'Regular')
    )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    size = models.CharField(choices=choices, max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.size


