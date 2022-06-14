from rest_framework import serializers

from store.models.cart_Item import CartItem
from store.models.product import Product
from store.serializers.simple_product_serializer import SimpleProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product =SimpleProductSerializer()        
    total_price =serializers.SerializerMethodField('get_total_price')
    def get_total_price(self, cart_item:CartItem):
        return cart_item.quantity * cart_item.product.unit_price

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    #quantity = serializers.IntegerField
    def validate_product_id(self, value):
        if not Product.objects.filter(pk = value).exists():
            raise serializers.ValidationError('No Product was found with the given ID was found!')
        return value
    # def validate_quantity(self, value):
    #     if value <= 0:
    #         raise serializers.ValidationError('Quantity can not be less then or equal to 0!')
    #     return value
    def save(self, **kwargs):
       cart_id = self.context['cart_id']
       product_id = self.validated_data['product_id']
       quantity = self.validated_data['quantity']
       try:
           cart_item = CartItem.objects.get(cart_id = cart_id, product_id = product_id)
           # update an exiting cart item
           cart_item.quantity += quantity
           cart_item.save()
           self.instance = cart_item
       except CartItem.DoesNotExist:
            # create a new cart item
            self.instance= CartItem.objects.create(cart_id = cart_id, **self.validated_data)

       return self.instance

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']

class UpdateCartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = ['quantity']