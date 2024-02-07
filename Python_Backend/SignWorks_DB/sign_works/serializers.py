from rest_framework import serializers
from .models import CustomerList, Permits

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerList
        fields = '__all__'


class PermitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permits
        fields = '__all__'