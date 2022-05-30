from django.db import models
from django.contrib import admin
from django.conf import settings

# customer

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default= MEMBERSHIP_BRONZE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name


    def __str__(self) -> str:
        return f'{self.user.first_name } {self.user.last_name}' 
    class Meta:
        ordering = ['user__first_name', 'user__last_name']