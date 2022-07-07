from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class SneakersViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SneakersSerializer

    def get_queryset(self):
        queryset = Sneaker.objects.all()
        sneaker_id = self.request.query_params.get('id')
        brand = self.request.query_params.get('brand')
        gender = self.request.query_params.get('gender')
        max_price = self.request.query_params.get('max')
        min_price = self.request.query_params.get('min')

        if gender == 'M':
            queryset = queryset.exclude(gender='W')
        elif gender == 'W':
            queryset = queryset.exclude(gender='M')

        if sneaker_id is not None:
            queryset = queryset.filter(id=sneaker_id)

        if brand is not None:
            queryset = queryset.filter(brand=brand)

        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)

        return queryset


class OrderListViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderListSerializer
    queryset = OrderList.objects.all()
