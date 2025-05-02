from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# myshop/urls.py

urlpatterns = [
    path('admin/',   admin.site.urls),
    path('cart/',    include('cart.urls', namespace='cart')),     # ← добавляем namespace
    path('',         include('products.urls')),
    path('users/',   include('users.urls')),
    path('orders/',  include('orders.urls')),
]


# Подключение статических файлов (например, изображения товаров, стилей и скриптов)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
