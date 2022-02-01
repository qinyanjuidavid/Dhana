from django.shortcuts import render
from django.http import (HttpResponseRedirect,
                         JsonResponse, HttpResponse)


def ProductView(request):
    context = {

    }
    return render(request, "shop/product_page.html", context)
