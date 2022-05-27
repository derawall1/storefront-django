from django.db import models

# Promotion 
class Promotion(models.Model):
    description = models.CharField(max_length= 255)
    discount = models.FloatField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()