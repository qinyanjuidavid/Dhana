from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from shop.models import (Brand, Category, Order,
                         OrderItem, Product, Rating)


def ProductView(request):
    productQuery = Product.objects.filter(available=True)
    context = {
        "products": productQuery,
    }
    return render(request, "shop/product_page.html", context)
