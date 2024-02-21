from rest_framework import serializers
from .models import CustomerList, Plans, Permits

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerList
        fields = '__all__'


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'


class PermitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permits
        fields = '__all__'