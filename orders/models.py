from django.db import models
from django.contrib.auth.models import User
from cart.models import CartItem

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"
