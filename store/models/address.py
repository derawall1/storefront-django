from django.core.validators import MinValueValidator
from django.db import models
from .customer import Customer
# address
class Address(models.Model):
    street = models.CharField(max_length= 255)
    city = models.CharField(max_length= 255)
    state = models.CharField(max_length= 255, null=True)
    zip_code = models.CharField(max_length=20, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)