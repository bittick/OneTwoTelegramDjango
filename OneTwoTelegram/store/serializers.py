from rest_framework import serializers
from .models import *


class SneakersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sneakers
        fields = '__all__'

