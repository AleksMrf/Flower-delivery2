from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from catalog.models import Flower
from orders.models import Order

User = get_user_model()

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.flower = Flower.objects.create(
            name='Розы',
            description='Красные розы',
            price=1000.00,
            available=True
        )

    def test_create_order(self):
        # Создаем заказ
        order = Order.objects.create(user=self.user)
        order.flowers.add(self.flower)
        self.assertEqual(order.user.username, 'testuser')
        self.assertEqual(order.flowers.first().name, 'Розы')
        self.assertEqual(order.status, 'P')  # Убедитесь, что статус по умолчанию 'P'

class OrderViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.flower = Flower.objects.create(
            name='Розы',
            description='Красные розы',
            price=1000.00,
            available=True
        )
        self.client.login(username='testuser', password='testpass123')


    def test_create_order_post(self):
        # Тестируем POST-запрос для создания заказа
        response = self.client.post(reverse('create_order'), {
            'flowers': [self.flower.id],
        })
        self.assertEqual(response.status_code, 302)  # Проверяем редирект после успешного создания
        self.assertEqual(Order.objects.count(), 1)  # Проверяем, что заказ создан