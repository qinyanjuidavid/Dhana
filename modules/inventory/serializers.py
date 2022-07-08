from unicodedata import category
from modules.inventory.models import Category, Product, Rating
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "category", "create_at",
                  "updated_at"
                  )

        read_only_fields = ("id",)


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ("id", "product_name", "unit_price",
                  "stock", "description", "category",
                  "image", "created_at", "updated_at")

        read_only_fields = ("id",)


class RatingSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ("id", "product", "rating",
                  "review", "customer", "created_at",
                  "updated_at",)
        read_only_fields = ("id",)
