from django.shortcuts import render
from apps.orders import views as order_views
from django.http import HttpResponse

# Create your views here.


def checkout(request):
    return HttpResponse("Checkout Page !")

def payment(request, order_id):
    return HttpResponse(f"Payment Page for Order {order_id}")
