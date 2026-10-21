from django.contrib import admin
from .models import Supplier, Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'supplier')



