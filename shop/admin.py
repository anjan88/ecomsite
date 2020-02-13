from django.contrib import admin
from shop.models import Products


# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title','price','discount_price','category','description','image')


admin.site.register(Products,ProductsAdmin)
