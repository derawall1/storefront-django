from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# views in django is equal to Request response handler, get the request and return response to user, api etc

@api_view()
def product_list(request):
    queryset = get_list_or_404(Product)
    serializer = ProductSerializer(queryset, many= True)
    return Response(serializer.data)

@api_view()
def product_detail(request, id):

    product =get_object_or_404(Product,pk = id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
  