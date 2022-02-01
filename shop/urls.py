from django.urls import path

from shop.views.views import ProductView

app_name = "shop"

urlpatterns = [
    path('products/', ProductView, name="home")
]
