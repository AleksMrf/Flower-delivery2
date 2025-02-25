from django.test import TestCase
from django.contrib.auth import get_user_model
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
        self.assertEqual(order.status, 'P')  # Статус по умолчанию

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

    def test_create_order_view(self):
        # Тестируем страницу оформления заказа
        response = self.client.get('/orders/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_form.html')

    def test_order_history_view(self):
        # Тестируем страницу истории заказов
        order = Order.objects.create(user=self.user)
        order.flowers.add(self.flower)
        response = self.client.get('/orders/history/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_history.html')
        self.assertContains(response, 'Розы')
