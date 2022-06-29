from .models import *
from rest_framework import viewsets, permissions
from .serializers import SneakersSerializer, SizesSneakersSerializer


class SneakersViewSet(viewsets.ModelViewSet):
    queryset = Sneakers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SneakersSerializer


class SizesSneakersViewSet(viewsets.ModelViewSet):
    queryset = SizesSneakers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SizesSneakersSerializer
