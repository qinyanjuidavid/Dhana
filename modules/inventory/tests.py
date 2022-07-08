from django.test import TestCase, Client
from modules.accounts.models import Customer, User
from modules.inventory.models import (Product,
                                      Category, Rating)
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse


class ProductTestCase(APITestCase):
    def setup(self):
        self.client = Client()

        self.category = Category.objects.create(
            category="Beverages"
        )

    def create_soda(self):
        return Product.objects.create(
            product_name="Sprite",
            unit_price=70.0,
            stock=5,
            description="Sprite 500ml",
            category=self.category,
            image="products/default.png",
        )

    def test_list_products(self):
        response = self.client.get(api_reverse("api:products"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

        sprite = self.create_soda()
        expected = [
            {
                'id': sprite.id,
                'product_name': 'sprite',
                'unit_price': 70.0,
                'stock': 5,
                'description': 'Sprite 500ml',
                # 'category':
                'image': 'products/default.png'
            }
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)


class CategoryTestCase(TestCase):
    def setup(self):
        self.client = Client()

    def create_beverage(self):
        return Category.objects.create(
            category="Beverages"
        )


class RatingTestCase(TestCase):
    def setup(self):
        self.client = Client()
        self.category = Category.objects.create(
            category="Beverages"
        )
        self.user = User.objects.create(
            username="testuser",
            full_name="test user",
            email="testuser@gmail.com",
            phone="+254712345678",
            role="Customer",
            is_active=True,
            is_admin=False,
            is_staff=False
        )
        self.customer = Customer.objects.create(
            user=self.user,
            bio="fly high",
            profile_picture="profile/default.png",
            city="sun city",
            address="151",
            postal_code="20116",
            town="river town",
            estate="villa estate"
        )
        self.coke = Product.objects.create(
            product_name="Coca-Cola",
            unit_price=80,
            stock=10,
            description="Coca-Cola 500ml",
            category=self.category,
            image="products/coke.png"
        )

    def create_rating(self):
        return Rating.objects.create(
            product=self.coke,
            rating=4,
            review="was not cold",
            customer=self.customer
        )
