from django.shortcuts import render
from product_app.models import Product


def home(request):
    products = Product.objects.all().order_by('-id')

    return render(request,
                  'products/index.html',
                  {'products': products})
