from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
import json

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
    http_method_names = ['get']
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderListSerializer
    queryset = OrderList.objects.all()


@api_view(['POST'])
def add_order(request):
    OrderInfo = json.loads(request.data)
    print(OrderInfo)
    order = OrderList(
        items=OrderInfo['items'],
        customer=OrderInfo['customer'],
        shipping_address=OrderInfo['shipping_address'],
        phone_number=OrderInfo['phone_number']
    )

    order.save()
    return Response(200)


@api_view(['GET'])
def get_order(request):
    list = OrderList.objects.all()
    # items = list.order_idOf.all()
    print(list)
    return Response(list)
