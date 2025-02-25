from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
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
