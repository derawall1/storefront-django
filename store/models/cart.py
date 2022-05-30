from django.db import models
from uuid import uuid4
# Cart
class Cart(models.Model):
    id = models.UUIDField(primary_key= True, default= uuid4)
    created_at = models.DateTimeField(auto_now_add=True)