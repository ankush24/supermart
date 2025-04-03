from django.contrib import admin
from .models import Product, Discount, CartItem


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("product", "min_discount_quantity", "discount_price")

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")