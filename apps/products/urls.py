from django.urls import path
from .views import product_list
from . import views # Import views from the current app (products)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('', views.product_list, name='product-list'),  # Route for /products/
    path('<int:product_id>/', views.product_detail, name='product-detail'),  # New detail page
]
