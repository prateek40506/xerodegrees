from django.shortcuts import render
from category.models import Category


def home(request):
    categories = Category.objects.all()
    context = {
        "category_row1": categories[0: 3],
        "category_row2": categories[3: 6],
        "category_row3": categories[6: 9],
        "category_row4": categories[9: 12],
        "category_row5": categories[12: 15],
        "category_row6": categories[15: 18],
        "category_row7": categories[18: 21],
    }
    return render(request, "home.html", context)

