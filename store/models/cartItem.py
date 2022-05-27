from django.db import models
from .cart import Cart
from .product import Product
# CartItem
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    quantity = models.PositiveSmallIntegerField()