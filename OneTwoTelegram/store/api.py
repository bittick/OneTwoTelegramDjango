from .models import *
from rest_framework import viewsets, permissions
from .serializers import SneakersSerializer, SizesSneakersSerializer


class SneakersViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SneakersSerializer

    def get_queryset(self):
        queryset = Sneakers.objects.all()

        id = self.request.query_params.get('id')
        brand = self.request.query_params.get('brand')
        gender = self.request.query_params.get('gender')

        if gender == 'M':
            queryset = queryset.exclude(gender='W')
        elif gender == 'W':
            queryset = queryset.exclude(gender='M')

        if id is not None:
            queryset = queryset.filter(id=id)

        if brand is not None:
            queryset = queryset.filter(brand=brand)

        return queryset
