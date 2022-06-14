from django.db import models

from store.validators import validate_file_size
from .product import Product

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'images')
    image = models.ImageField(
            upload_to='store/images',
            validators = [validate_file_size]        
        )