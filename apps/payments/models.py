from django.db import models
from django.contrib.auth.models import User
from apps.cart.models import Order, OrderItem



class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, choices=[("Success", "Success"), ("Failed", "Failed")])
