from modules.inventory.serializers import ProductSerializer
from modules.orders.models import Order, OrderItem
from rest_framework.serializers import ModelSerializer


class OrderItemSerializer(ModelSerializer):
    item = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ("id", "item", "item", "quantity",
                  "customer", 'total', "created_at",
                  "updated_at")

        read_only_fields = ("id",)


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "items", "total", "customer",
                  "created_at", "updated_at")

        read_only_fields = ("id",)
