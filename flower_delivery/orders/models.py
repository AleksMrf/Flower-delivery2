from django.db import models
from accounts.models import User
from catalog.models import Flower

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

    def __str__(self):
        return f"Заказ №{self.id} ({self.get_status_display()})"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
