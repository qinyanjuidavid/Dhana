from accounts.models import Customer, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse
from shop.models import Brand, Category, Order, OrderItem, Product, Rating
from django.utils import timezone


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


@login_required
def addToCartView(request, id):
    productQs = Product.objects.get(id=id)
    orderItem, created = OrderItem.objects.get_or_create(
        product=productQs,
        customer=Customer.objects.get(
            user=request.user
        ),
        ordered=False,
    )
    order = Order.objects.filter(product=orderItem)

    if order.exists():
        order = order[0]
        if order.product.filter(product__id=productQs.id,
                                ordered=False,
                                ).exists():
            orderItem.quantity += 1
            orderItem.save()
            messages.success(request,
                             "Shoe quantity was added successfully!")
        else:
            order.product.add(orderItem)
            messages.success(
                request, "Shoe was successfully added to the cart.")
    else:
        date_ordered = timezone.now()
        order = Order.objects.create(
            date_ordered=date_ordered,
            customer=Customer.objects.get(
                user=request.user
            )
        )
        order.product.add(orderItem)
        order.save()
        messages.success(
            request, "Shoe was successfully added to the cart!"
        )
    return HttpResponseRedirect(f"/product/{id}/details/")


@login_required
def removeFromCart(request, id):
    productQs = Product.objects.get(id=id)
    orderItem, created = OrderItem.objects.get_or_create(
        product=productQs,
        customer=Customer.objects.get(
            user=request.user
        ),
        ordered=False
    )
    order = Order.objects.filter(
        product=OrderItem
    )
    if order.exists():
        order = order[0]
        if order.product.filter(product__id=productQs.id,
                                ordered=False
                                ).exists():
            if orderItem.quantity > 1:
                orderItem.quantity -= 1
                orderItem.save()
                messages.info(
                    request,
                    "Show quantity was successfully removed"
                )
            else:
                order.product.remove(orderItem)
                messages.warning(
                    request,
                    "The shoe was successfully removed from cart."
                )
        else:
            pass
    else:
        pass


def cartView(request):
    context = {

    }
    return render(request, "shop/cart.html", context)


def checkoutView(request):
    context = {

    }
    return render(request, "shop/checkout.html", context)


@login_required
def profileView(request):
    context = {

    }
    return render(request, "shop/customerProfile.html", context)
