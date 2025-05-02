# orders/views.py
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.models import CartItem
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        order = Order.objects.create(user=request.user, address=address)

        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        # Очищаем корзину
        cart_items.delete()

        return render(request, 'orders/success.html', {'order': order})
    return render(request, 'orders/checkout.html')
