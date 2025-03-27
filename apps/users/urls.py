from django.urls import path
from . import views

urlpatterns = [
    # path('', users, name='users-home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    # path('login/', login_view, name='login')
]
