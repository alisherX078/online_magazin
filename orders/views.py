from django.shortcuts import render, redirect
from .models import Order
from cart.models import CartItem
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        order = Order.objects.create(user=request.user, address=address)
        CartItem.objects.filter(user=request.user).delete()
        return render(request, 'orders/success.html', {'order': order})
    return render(request, 'orders/checkout.html')
