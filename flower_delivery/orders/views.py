from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, Cart, CartItem, OrderItem
from catalog.models import Flower


@login_required
def create_order(request):
    if request.method == 'POST':
        flowers_ids = request.POST.getlist('flowers')
        flowers = Flower.objects.filter(id__in=flowers_ids)
        order = Order.objects.create(user=request.user)
        order.flowers.set(flowers)
        return redirect('order_history')  # Перенаправление на историю заказов
    else:
        flowers = Flower.objects.all()
        return render(request, 'orders/order_form.html', {'flowers': flowers})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required
def add_to_cart(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, flower=flower)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('catalog_home')

@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'orders/cart.html', {'cart': cart})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    order = Order.objects.create(user=request.user)

    for item in cart.items.all():
        OrderItem.objects.create(order=order, flower=item.flower, quantity=item.quantity)

    cart.items.all().delete()  # Очистка корзины после оформления заказа
    return redirect('order_history')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})


