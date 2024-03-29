from rest_framework import serializers
from .models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ('title', )


class SizesSneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizesSneaker
        exclude = ('sneaker_id', 'id')


class SneakersSerializer(serializers.ModelSerializer):
    sizes = SizesSneakerSerializer()
    brand = serializers.StringRelatedField()

    class Meta:
        model = Sneaker
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = OrderList
        fields = '__all__'

