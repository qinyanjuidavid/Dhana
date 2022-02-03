from django.urls import path

from shop.views.templates_views import ProductView

app_name = "shop"

urlpatterns = [
    path('', ProductView, name="home")
]
