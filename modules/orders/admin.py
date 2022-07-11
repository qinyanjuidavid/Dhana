from django.contrib import admin
from modules.orders.models import Order, OrderItem

admin.site.register(OrderItem)
admin.site.register(Order)
