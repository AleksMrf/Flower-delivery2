from django.db import models
from accounts.models import User  # Импорт модели User из accounts
from catalog.models import Flower

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.flower.name} (x{self.quantity})"

class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'В обработке'),
        ('C', 'Завершен'),
        ('X', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    flowers = models.ManyToManyField(Flower, verbose_name='Цветы')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    address = models.TextField(verbose_name='Адрес доставки', blank=True, null=True)  # Добавлено поле address

    def __str__(self):
        return f"Заказ №{self.id} ({self.get_status_display()})"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.flower.name} (x{self.quantity})"