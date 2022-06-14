from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from store.models import Customer

class UserCreateSerializer(BaseUserCreateSerializer):    
  
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

  