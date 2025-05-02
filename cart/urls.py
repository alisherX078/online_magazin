# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='cart_add'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='cart_remove'),
    path('detail/', views.cart_detail, name='cart_detail'),  # Убедись, что здесь указан правильный путь
]
