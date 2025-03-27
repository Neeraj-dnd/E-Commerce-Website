from django.shortcuts import render
from apps.products.models import Product

def homepage(request):
    featured_products = Product.objects.all()[:6]
    return render(request, "homepage/homepage.html", {"products": featured_products})
