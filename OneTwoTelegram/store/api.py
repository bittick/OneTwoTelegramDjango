from .models import *
from rest_framework import viewsets, permissions
from .serializers import SneakersSerializer, SizesSneakersSerializer


class SneakersViewSet(viewsets.ModelViewSet):
    # queryset = SizesSneakers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SizesSneakersSerializer

    def get_queryset(self):
        queryset = SizesSneakers.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(sneaker_id=id)
        return queryset
