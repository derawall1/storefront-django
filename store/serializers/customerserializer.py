from rest_framework import serializers

from store.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only =True)
    # first_name = serializers.CharField(max_length = 255, read_only=True)
    # last_name = serializers.CharField(max_length = 255, read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'user_id','phone', 'birth_date', 'membership']