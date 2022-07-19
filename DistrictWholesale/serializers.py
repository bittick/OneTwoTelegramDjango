from rest_framework import serializers
from .models import *


class VegetableSerializer(serializers.ModelSerializer):
    product_cat = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
