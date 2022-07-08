from modules.inventory.views import CategoryAPIView, ProductAPIView, RatingAPIView
from rest_framework.routers import SimpleRouter
from django.urls import path


app_name = "api"
routes = SimpleRouter()

routes.register("products", ProductAPIView, basename="products")
routes.register("category", CategoryAPIView, basename="category")
routes.register("rating", RatingAPIView, basename="rating")
urlpatterns = [
    *routes.urls,
]
