from modules.inventory.views import CategoryAPIView, ProductAPIView, RatingAPIView
from modules.orders.views import OrderAPIView
from rest_framework.routers import SimpleRouter
from django.urls import path


app_name = "api"
routes = SimpleRouter()

# Products routes
routes.register("products", ProductAPIView, basename="products")
routes.register("category", CategoryAPIView, basename="category")
routes.register("rating", RatingAPIView, basename="rating")

# Order routes
routes.register("orders", OrderAPIView, basename='orders')
urlpatterns = [
    *routes.urls,
]
