from rest_framework import serializers
from .models import *


class SneakersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sneakers
        fields = '__all__'


class SizesSneakersSerializer(serializers.ModelSerializer):
    sneak_description = serializers.CharField(source='sneaker.description')
    sneak_title = serializers.CharField(source='sneaker.title')
    sneak_price = serializers.CharField(source='sneaker.price')
    sneak_id = serializers.CharField(source='sneaker.id')

    class Meta:
        model = SizesSneakers
        fields = ('sneak_id', 'sneak_title', 'sneak_price', 'sneak_description', 'size_34',
                  'size_35', 'size_36', 'size_37', 'size_38', 'size_39', 'size_40',
                  'size_41', 'size_42', 'size_43', 'size_44', 'size_45')

