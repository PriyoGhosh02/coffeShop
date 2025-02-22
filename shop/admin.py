from django.contrib import admin
from .models import Product, Order, CartItem, Customer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Ensure these fields exist in Product
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'status', 'created_at')  # Ensure these fields exist in Order
    list_filter = ('status',)
    search_fields = ('customer__user__username',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')  # Ensure these fields exist in CartItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'address')  # Ensure these fields exist in Customer
