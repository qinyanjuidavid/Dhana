from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from shop.models import (Brand, Category, Order,
                         OrderItem, Product, Rating)


def ProductView(request):
    productQuery = Product.objects.filter(available=True)
    categoryQs = Category.objects.all()
    context = {
        "products": productQuery,
        "categories": categoryQs
    }
    return render(request, "shop/product_page.html", context)


def productDetailsView(request, id):
    productObj = Product.objects.get(available=True, id=id)
    context = {
        "product": productObj
    }
    return render(request, "shop/product_details.html", context)


def cartView(request):
    context = {

    }
    return render(request, "shop/cart.html", context)


def checkoutView(request):
    context = {

    }
    return render(request, "shop/checkout.html", context)
