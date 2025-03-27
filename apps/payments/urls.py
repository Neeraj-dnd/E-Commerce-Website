from django.urls import path, include
from .views import payments_view  # Import a test view
from . import views

app_name = 'payments' 

urlpatterns = [
    path('', payments_view, name='payments'),
    path('payment/<int:order_id>/', views.payments_view, name='payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    # path('checkout/', order_views.checkout, name='checkout'),
    # path('payment/<int:order_id>/', order_views.payment, name='payment'),
]
