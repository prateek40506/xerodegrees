from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name="menu"),
    path('category/<slug:category_slug>/', views.menu, name='items_by_category'),
    path('category/<slug:category_slug>/<slug:item_slug>/', views.item_details, name='item_details'),
]
