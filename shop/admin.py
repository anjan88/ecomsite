from django.contrib import admin
from shop.models import Products, Order

# Register your models here.

admin.site.site_header = "E-Commerce site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage  ABC Shopping"


class ProductsAdmin(admin.ModelAdmin):
    # working on the actions
    def change_category_to_Electronics(self, request, queryset):
        queryset.update(category="Electronics")

    def change_category_to_adventures(self, request, queryset):
        queryset.update(category="Adventures")
    # shortining the length of the action words used
    change_category_to_Electronics.short_description = 'Electronics Category'
    change_category_to_adventures.short_description = 'Adventures Category'
    # displaying al fields
    list_display = ('title', 'price', 'discount_price', 'category', 'description', 'image')
    # using searchfield
    search_fields = ('title', 'category',)
    # Actions to display
    actions = ('change_category_to_Electronics', 'change_category_to_adventures',)
    # to make fields editable
    list_editable = ('price','category','discount_price','description', 'image')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'city', 'state', 'zipcode', 'total')


admin.site.register(Products, ProductsAdmin)
admin.site.register(Order, OrderAdmin)
