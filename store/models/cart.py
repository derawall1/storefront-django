from django.db import models

# Cart
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)