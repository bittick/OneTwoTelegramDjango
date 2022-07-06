from .models import *
from rest_framework import viewsets, permissions
from .serializers import SneakersSerializer


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
        max_price = self.request.query_params.get('max')
        min_price = self.request.query_params.get('min')

        if gender == 'M':
            queryset = queryset.exclude(gender='W')
        elif gender == 'W':
            queryset = queryset.exclude(gender='M')

        if id is not None:
            queryset = queryset.filter(id=id)

        if brand is not None:
            queryset = queryset.filter(brand=brand)

        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)

        return queryset
