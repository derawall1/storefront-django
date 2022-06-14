from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from store.models import Order, Customer
from store.serializers import OrderSerializer, CreateOrderSerializer, UpdateOrderSerializer


class OrderViewSet(ModelViewSet):  
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
       serializer =CreateOrderSerializer(
            data=request.data, 
            context = {'user_id': self.request.user.id}
           )
       serializer.is_valid(raise_exception= True)
       order =serializer.save()
       serializer=OrderSerializer(order)
       return Response(serializer.data)


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer
   
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()

        customer_id = Customer.objects.only('id').get(user_id = user.id)
        return Order.objects.filter(customer_id = customer_id)