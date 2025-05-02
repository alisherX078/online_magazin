# cart/views.py
from django.shortcuts import redirect, render, get_object_or_404

from .cart import Cart
from .models import CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total() for item in items)
    return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})


@login_required
def remove_from_cart(request, item_id):
    CartItem.objects.get(id=item_id, user=request.user).delete()
    return redirect('cart:cart_detail')


@login_required
def cart_add(request, product_id):
    if request.method == 'POST':
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        return redirect('cart:cart_detail')
    else:
        # Отправить ошибку или просто перенаправить
        return redirect('cart:cart_detail')
