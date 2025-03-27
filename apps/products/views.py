from django.shortcuts import get_object_or_404, render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Fetch the product
    return render(request, 'products/product_detail.html', {'product': product})

