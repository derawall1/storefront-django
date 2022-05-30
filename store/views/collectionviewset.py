from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from store.models import Collection
from store.permissions import IsAdminOrReadOnly
from store.serializers import CollectionSerializer

class CollectionViewSet(ModelViewSet):
    queryset =Collection.objects.annotate(products_count = Count('products'))
    serializer_class = CollectionSerializer    
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        collection =get_object_or_404(Collection.objects.annotate(products_count = Count('products')),pk = kwargs['pk'])
        if collection.products.count() >0:
            return Response({'error': 'collection can not be deleted because it is associated with an order item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

    