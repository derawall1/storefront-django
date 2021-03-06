

from rest_framework import serializers

from store.models.cart import Cart
from store.serializers.cart_item_serializer import CartItemSerializer

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    items =CartItemSerializer(many=True, read_only =True)
    total_price = serializers.SerializerMethodField('get_total_price')

    def get_total_price(self, cart:Cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']