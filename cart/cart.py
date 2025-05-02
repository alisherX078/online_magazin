# cart/cart.py
from products.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session.modified = True

    from products.models import Product

    def remove(self, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            # Handle product not found case
            return
        product_id = str(product.id)  # Now 'product' is an instance
        # Continue with your removal logic

    def get_items(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_total(self):
        total = 0
        for item in self.cart.values():
            total += float(item['price']) * item['quantity']
        return total
