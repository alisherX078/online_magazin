# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'       # ← очень важно!
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
]
