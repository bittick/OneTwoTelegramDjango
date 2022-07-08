from rest_framework import serializers
from .models import *


class SneakersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sneaker
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    delivered = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = OrderList
        fields = '__all__'
