from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_disply = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)