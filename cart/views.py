# cart/views.py
from django.shortcuts import redirect, render, get_object_or_404
from .models import CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    """Добавляет товар в корзину."""
    product = get_object_or_404(Product, id=product_id)

    # Проверяем, есть ли уже товар в корзине
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        # Если товар уже в корзине, увеличиваем его количество
        item.quantity += 1
        item.save()

    return redirect('product_list')  # или куда нужно

@login_required
def cart_detail(request):
    """Отображает содержимое корзины."""
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total() for item in items)  # Предполагаем, что get_total() возвращает стоимость товара с учетом количества
    return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    """Удаляет товар из корзины."""
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()  # Удаляем элемент из базы данных
    return redirect('cart:cart_detail')

from django.shortcuts import redirect
from .cart import Cart

def cart_remove(request, item_id):
    """Удаляет товар из корзины, используя объект Cart."""
    cart = Cart(request)
    cart.remove(item_id)
    return redirect('cart:cart_detail')