# from django.shortcuts import get_list_or_404
# from rest_framework.decorators import api_view
# from rest_framework.generics import ListCreateAPIView
# from ..models import Product
# from ..serializers import ProductSerializer

# class ProductList(ListCreateAPIView):
#     queryset = get_list_or_404(Product.objects.select_related('collection'))
#     serializer_class = ProductSerializer    

#     def get_serializer_context(self):
#         return{'request': self.request}