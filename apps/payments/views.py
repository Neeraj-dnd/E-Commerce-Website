from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from apps.cart.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings
from django.http import JsonResponse
from apps.products.models import Product



# def payment(request, order_id):
    # order = Order.objects.get(id=order_id)
    # client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # payment_data = {
    #     "amount": int(order.total_price * 100),  # Convert to paisa
    #     "currency": "INR",
    #     "receipt": f"order_{order.id}",
    #     "payment_capture": 1,
    # }

    # payment = client.order.create(payment_data)
    # return render(request, "payments/payment.html", {"payment": payment, "order": order})

def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    try:
        import razorpay
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        razorpay_order = client.order.create({
            "amount": int(order.total_price * 100),
            "currency": "INR",
            "payment_capture": "1"
        })
    except Exception as e:
        print("⚠️ Razorpay mock mode activated:", e)
        # mock order dict
        razorpay_order = {
            "id": "order_mock_12345",
            "amount": int(order.total_price * 100),
            "currency": "INR"
        }

    context = {
        "razorpay_order_id": razorpay_order["id"],
        "order": order,
        "amount": razorpay_order["amount"]
    }

    return render(request, "payments/payment.html", context)


def payment_success(request):
    if request.method == 'POST':
        # For now, get the latest order (you can adjust logic based on your setup)
        order = Order.objects.latest('id')
        order.status = "Paid"
        order.save()

        return render(request, "payments/success.html", {"order": order})
    return redirect("cart:view_cart") 


def payments_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'payments/payment.html', {'order': order})
