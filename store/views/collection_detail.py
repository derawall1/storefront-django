# from django.shortcuts import get_object_or_404
# from django.db.models.aggregates import Count
# from rest_framework.response import Response
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# from rest_framework import status
# from ..models import Collection
# from ..serializers import CollectionSerializer


# # collection api actions
# class CollectionDetail(RetrieveUpdateDestroyAPIView):
   
#     queryset =Collection.objects.annotate(products_count = Count('products'))
#     serializer_class = CollectionSerializer    

#     def delete(self, reqeust, pk):
#         collection =get_object_or_404(Collection.objects.annotate(products_count = Count('products')),pk = pk)
#         if collection.products.count() >0:
#             return Response({'error': 'collection can not be deleted because it is associated with an order item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)