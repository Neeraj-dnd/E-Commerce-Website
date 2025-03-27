from django.shortcuts import redirect, render, get_object_or_404
from apps.products.models import Product
from .cart import Cart
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def cart_add(request, product_id):
    """Add item to cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect('cart:cart-detail')

def cart_remove(request, product_id):
    """Remove item from cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart-detail')

def cart_detail(request):
    """Show cart contents"""
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@login_required(login_url='/login/')
def checkout(request):
    # Get the cart from session
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

    if request.method == "POST":
        # Create order on POST
        user = request.user
        order = Order.objects.create(user=user, total_price=total_price, status="Pending")

        for product_id, item in cart.items():
            try:
                product = Product.objects.get(id=int(product_id))
                product_name = product.name
            except Product.DoesNotExist:
                product_name = f"Unknown Product (ID: {product_id})"

            OrderItem.objects.create(
                order=order,
                product_name=product_name,
                quantity=item['quantity'],
                price=item['price']
            )

        # Clear cart after checkout
        request.session['cart'] = {}
        return redirect("payments:payment", order_id=order.id)

    # On GET: Show checkout page with order summary
    return render(request, "cart/checkout.html", {
        "cart": cart.values(),
        "total_price": total_price,
    })
