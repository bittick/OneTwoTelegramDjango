from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import api_view, action, parser_classes
from rest_framework.response import Response
import json
from rest_framework.parsers import JSONParser

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
    http_method_names = ['get', 'post']
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderListSerializer
    queryset = OrderList.objects.all()


@api_view(['POST', 'GET'])
@parser_classes([JSONParser])
def add_order(request):
    order_info = request
    print(type(request), request.__dict__)
    # order = OrderList(
    #     customer=order_info['order_list']['customer'],
    #     shipping_address=order_info['order_list']['shipping_address'],
    #     phone_number=order_info['order_list']['phone_number']
    # )
    # print(order)
    # # order.save()
    # for item in order_info['order_items']:
    #     cur_item = OrderItem(
    #         order_id=order.id,
    #         sneaker_id=item['sneaker_id'],
    #         sneaker_size=item['sneaker_size'],
    #         quantity=item['quantity']
    #     )
    #     print(cur_item)
    #     # cur_item.save()
    return Response(200)


# @api_view(['GET'])
# def get_order(request):
#     list = OrderList.objects.all()
#     # items = list.order_idOf.all()
#     a = json.dumps(list)
#     return Response(a)
