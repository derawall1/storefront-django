
# from django.shortcuts import get_list_or_404
# from django.db.models.aggregates import Count
# from rest_framework.generics import ListCreateAPIView
# from ..models import Collection
# from ..serializers import CollectionSerializer

# class CollectionList(ListCreateAPIView):
#     queryset = get_list_or_404(Collection.objects.annotate(products_count = Count('products')))
#     serializer_class = CollectionSerializer

#     def get_serializer_context(self):
#         return {'request': self.request}  