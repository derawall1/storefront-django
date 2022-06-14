
from decimal import Decimal
from rest_framework import serializers

from store.models import Product
from store.serializers.product_image_serializer import ProductImageSerializer


       
# product serializer

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many =True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', \
             'unit_price','price_with_tax', 'collection', 'last_update', 'images']
       
    #price = serializers.DecimalField(max_digits=6, decimal_places=2, source ='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
    #collection = CollectionSerializer()
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name= 'collection-detail'
    # )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)