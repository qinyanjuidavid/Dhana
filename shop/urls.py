from django.urls import path

from shop.views.templates_views import (ProductView,
                                        productDetailsView,
                                        cartView, checkoutView
                                        )

app_name = "shop"

urlpatterns = [
    path('', ProductView, name="home"),
    path('product/<id>/details/',
         productDetailsView,
         name="productDetails"),
    path('cart/', cartView, name="cart"),
    path("checkout/",
         checkoutView,
         name="checkout")
]
