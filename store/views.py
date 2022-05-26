
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework import status
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer

# views in django is equal to Request response handler, get the request and return response to user, api etc

# product api actions
class ProductList(ListCreateAPIView):
    def get_queryset(self):
        return get_list_or_404(Product.objects.select_related('collection'))

    def get_serializer(self, *args, **kwargs):
        return ProductSerializer

    def get_serializer_context(self):
        return{'request': self.request}
    def get(self, request):
        queryset = get_list_or_404(Product.objects.select_related('collection'))
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class ProductDetail(APIView):
    def get(self,request, id):
        product =get_object_or_404(Product,pk = id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self,request, id):
        product =get_object_or_404(Product,pk = id)
        serializer = ProductSerializer(product, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, reqeust, id):
        product =get_object_or_404(Product,pk = id)
        if product.orderitems.count() >0:
            return Response({'error': 'product can not be deleted because it is associated with an order item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        


# collection api actions
class CollectionDetail(APIView):
    def get(self,request, pk):
        collection =get_object_or_404(Collection.objects.annotate(products_count = Count('products')),pk = pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    
    def put(self,request, pk):

        collection =get_object_or_404(Collection.objects.annotate(products_count = Count('products')),pk = pk)
        serializer = CollectionSerializer(collection, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, reqeust, pk):
        collection =get_object_or_404(Collection.objects.annotate(products_count = Count('products')),pk = pk)
        if collection.products.count() >0:
            return Response({'error': 'collection can not be deleted because it is associated with an order item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class CollectionList(APIView):
    def get(self, reqeust):
        queryset = get_list_or_404(Collection.objects.annotate(products_count = Count('products')))
        serializer = CollectionSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)



        

  