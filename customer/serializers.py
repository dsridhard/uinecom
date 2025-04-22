from rest_framework import serializers
from .models import Customer
from .models import Address
from .models import CustomerProfile
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerProfile
        fields='__all__'        

