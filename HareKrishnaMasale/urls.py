"""
URL configuration for HareKrishnaMasale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include

from .views import homepage
from django.conf import settings
from django.conf.urls.static import static
from apps.orders import views as order_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Landing page
    path("", homepage, name="homepage"),

    # Custom login/logout views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),


    # App includes
    path('products/', include('apps.products.urls')),
    path('cart/', include(('apps.cart.urls', 'cart'), namespace='cart')),
    path('users/', include(('apps.users.urls', 'users'), namespace='users')),
    path('payments/', include(('apps.payments.urls', 'payments'), namespace='payments')),
]

# Add media URL settings
if settings.DEBUG:  # Only serve media in development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)