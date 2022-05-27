from django.db import models
from .order import Order
from .product import Product

# OrderItem
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete= models.PROTECT)
    product = models.ForeignKey(Product, on_delete= models.PROTECT, related_name='orderitems')   
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)