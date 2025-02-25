from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        # Создаем пользователя
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            phone='1234567890'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.phone, '1234567890')
        self.assertTrue(user.check_password('testpass123'))

    def test_create_superuser(self):
        # Создаем суперпользователя
        admin_user = User.objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class UserViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_login_view(self):
        # Тестируем страницу входа
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_register_view(self):
        # Тестируем страницу регистрации
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
