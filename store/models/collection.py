from django.db import models
#from .product import Product

# Collections
class Collection(models.Model):
    title = models.CharField(max_length= 255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']  