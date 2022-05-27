
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# from rest_framework import status
# from ..models import Product
# from ..serializers import ProductSerializer

# class ProductDetail(RetrieveUpdateDestroyAPIView):
    
#     queryset =Product.objects.all()
#     serializer_class = ProductSerializer
#     #lookup_field = 'id'
    
#     def delete(self, reqeust, pk):
#         product =get_object_or_404(Product,pk = pk)
#         if product.orderitems.count() >0:
#             return Response({'error': 'product can not be deleted because it is associated with an order item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)