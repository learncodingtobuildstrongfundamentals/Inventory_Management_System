from django.urls import path
from . import views
urlpatterns = [
    path('inven/', views.inventory_view, name='inventory'),
    path('products/', views.product_view, name='products'),
]

