from django.db import transaction
from django.forms import ValidationError
from rest_framework import serializers
from store.models import Order, OrderItem, CartItem, Cart
from store.models.customer import Customer
from store.serializers import SimpleProductSerializer
from store.signals import order_created

class OrderItemSerializer(serializers.ModelSerializer):
    product =SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'unit_price', 'quantity']



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'placed_at', 'payment_status', 'items']

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk = cart_id).exists():
            raise serializers.ValidationError('No cart with the given ID was found!')
        if CartItem.objects.filter(cart_id = cart_id).count() == 0:
            raise serializers.ValidationError('The cart is empty!')

        return cart_id

    def save(self, **kwargs):
        with transaction.atomic():

            cart_id =self.validated_data['cart_id']
            #print(self.context['user_id'])
            user_id =self.context['user_id']
            customer = Customer.objects.get(user_id = user_id)
            order = Order.objects.create(customer = customer)
            cart_items = CartItem.objects.select_related('product').filter(cart_id = cart_id)
            order_items =  [
                OrderItem(
                    order = order,
                    product = item.product,
                    unit_price = item.product.unit_price,
                    quantity = item.quantity

                ) for item in cart_items
            ]

            OrderItem.objects.bulk_create(order_items)

            Cart.objects.filter(pk = cart_id).delete()
            order_created.send_robust(self.__class__, order = order)
            return order