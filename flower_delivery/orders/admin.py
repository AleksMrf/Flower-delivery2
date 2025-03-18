from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

# Регистрация модели Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)

# Регистрация модели CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'flower', 'quantity')
    search_fields = ('cart__user__username', 'flower__name')

# Регистрация модели Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)

# Регистрация модели OrderItem
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'flower', 'quantity')
    search_fields = ('order__user__username', 'flower__name')
