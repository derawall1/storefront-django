
from rest_framework import serializers

from store.models import Product


       
# simple product serializer

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']
       
    