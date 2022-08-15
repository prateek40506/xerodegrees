from django.shortcuts import render
from .models import MenuItem, Size, AddOns
from django.core.paginator import Paginator
from category.models import Category
# Create your views here.


def menu(request, category_slug=None):
    menu_items = []
    if request.method == "POST":
        min_price = int(request.POST['min_price'])
        max_price = int(request.POST['max_price'])
        if category_slug:
            is_items = MenuItem.objects.filter(category__slug=category_slug).exists()
            if is_items:
                menu_items = MenuItem.objects.filter(category__slug=category_slug)
        else:
            menu_items = MenuItem.objects.all()
        query_items = []
        for item in menu_items:
            if item.is_size():
                sizes = Size.objects.filter(menu_item=item)
                for size in sizes:
                    if min_price <= size.price <= max_price:
                        query_items.append(item)
                        break
            else:
                if min_price <= item.price <= max_price:
                    query_items.append(item)
        paginator = Paginator(query_items, 9)
        page = request.GET.get('page')
        paged_items = paginator.get_page(page)
        context = {
            "items": paged_items,
            "counter": len(query_items),
            "category_slug": category_slug
        }

    else:
        if category_slug:
            is_items = MenuItem.objects.filter(category__slug=category_slug).exists()
            if is_items:
                menu_items = MenuItem.objects.filter(category__slug=category_slug)
        else:
            menu_items = MenuItem.objects.all()
        paginator = Paginator(menu_items, 9)
        page = request.GET.get('page')
        paged_items = paginator.get_page(page)
        context = {
            "items": paged_items,
            "counter": len(menu_items),
            "category_slug": category_slug
        }
    return render(request, 'foodmenu.html', context)


def item_details(request, category_slug, item_slug):
    try:
        single_item = MenuItem.objects.get(category__slug=category_slug, slug=item_slug)
        addon = None
        addon_description = None
        if category_slug == "hot-coffee":
            addon_description = "ADD ON FLAVOURS"
            addon = "Flavours"
        elif category_slug == "single-serve-pizzas":
            addon_description = "MAKE IT CHEESY @29/-"
            addon = "Cheesy"
        elif category_slug == "pizza-in-a-jar":
            addon_description = "MAKE IT PERI PERI @39/-"
            addon = "Peri Peri"
        elif category_slug == "special-pizzas":
            addon_description = "MAKE IT CHEESY!!"
            addon = "Cheesy"
        elif category_slug in ("chicken-strips", "chicken-wings"):
            addon_description = "ADD SAUCES!!"
            addon = "Sauces"
        context = {
            "single_item": single_item,
            "addon_description": addon_description,
            "addon": addon
        }
    except Exception as e:
        raise e
    return render(request, "item_page.html", context)


