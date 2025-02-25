from django.test import TestCase
from catalog.models import Flower

class FlowerModelTest(TestCase):
    def test_create_flower(self):
        # Создаем цветок
        flower = Flower.objects.create(
            name='Розы',
            description='Красные розы',
            price=1000.00,
            available=True
        )
        self.assertEqual(flower.name, 'Розы')
        self.assertEqual(flower.description, 'Красные розы')
        self.assertEqual(flower.price, 1000.00)
        self.assertTrue(flower.available)

class FlowerViewsTest(TestCase):
    def setUp(self):
        self.flower = Flower.objects.create(
            name='Розы',
            description='Красные розы',
            price=1000.00,
            available=True
        )

    def test_catalog_home_view(self):
        # Тестируем главную страницу каталога
        response = self.client.get('/catalog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/list.html')
        self.assertContains(response, 'Розы')

    def test_flower_detail_view(self):
        # Тестируем страницу деталей цветка
        response = self.client.get(f'/catalog/{self.flower.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/detail.html')
        self.assertContains(response, 'Красные розы')
