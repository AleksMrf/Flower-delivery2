from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:flower_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('create/', views.create_order, name='create_order'),
    path('history/', views.order_history, name='order_history'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]