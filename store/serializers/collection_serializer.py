from rest_framework import serializers

from store.models import Collection

# collection serializer object
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
        read_only_fields = ('products_count', )
    products_count = serializers.IntegerField(read_only=True)