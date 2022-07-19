from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from django.forms.models import model_to_dict


# class SneakersViewSet(viewsets.ModelViewSet):
#     http_method_names = ['get']
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = SneakersSerializer
#
#     def get_queryset(self):
#         queryset = Sneaker.objects.all()
#         sneaker_id = self.request.query_params.get('id')
#         brand = self.request.query_params.get('brand')
#         gender = self.request.query_params.get('gender')
#         max_price = self.request.query_params.get('max')
#         min_price = self.request.query_params.get('min')
#
#         if gender == 'M':
#             queryset = queryset.exclude(gender='W')
#         elif gender == 'W':
#             queryset = queryset.exclude(gender='M')
#
#         if sneaker_id is not None:
#             queryset = queryset.filter(id=sneaker_id)
#
#         if brand is not None:
#             queryset = queryset.filter(brand=brand)
#
#         if max_price is not None:
#             queryset = queryset.filter(price__lte=max_price)
#
#         if min_price is not None:
#             queryset = queryset.filter(price__gte=min_price)
#
#         return queryset


class OrderListViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderListSerializer
    queryset = OrderList.objects.all()


@api_view(['POST'])
def add_order(request):
    order_info = json.loads(request.body.decode("utf-8"))
    order = OrderList(
        customer=order_info['order_list']['customer'],
        shipping_address=order_info['order_list']['shipping_address'],
        phone_number=order_info['order_list']['phone_number'],
        is_paid=True
    )
    for item in order_info['order_items']:
        if not Sneaker.objects.filter(id=item['sneaker_id']).exists():
            return Response({'e': 'No such sneaker_id'}, status.HTTP_400_BAD_REQUEST)
    order.save()
    for item in order_info['order_items']:
        sneaker = Sneaker.objects.get(id=item['sneaker_id'])
        cur_item = OrderItem(
            order_id=order,
            sneaker_id=sneaker,
            sneaker_size=item['sneaker_size'],
            quantity=item['quantity']
        )
        cur_item.save()
    return Response({'order_id': order.order_id}, status.HTTP_200_OK)


@api_view(['GET'])
def check_server(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def filter_sneakers(request):
    print(request)
    filter_data = json.loads(request.body)
    keys = list(filter_data.keys())
    kwargs = {}
    response = []
    if keys == ['sizes']:
        sneakers = Sneaker.objects.all()
    else:
        if 'brand' in keys:
            kwargs['brand'] = Brand.objects.get(title=filter_data['brand'])
        if 'color' in keys:
            kwargs['color'] = filter_data['color']
        if 'min_price' in keys:
            kwargs['price__gte'] = filter_data['min_price']
        if 'max_price' in keys:
            kwargs['price__lte'] = filter_data['max_price']
        sneakers = Sneaker.objects.filter(**kwargs)
        if 'gender' in keys:
            if filter_data == 'M':
                sneakers = sneakers.exclude(gender='W')
            elif filter_data == 'W':
                sneakers = sneakers.exclude(gender='M')
    if 'sizes' in keys:
        sizes = []
        for i in filter_data['sizes']:
            sizes.append('size_' + i)
        tmp = []
        for sneaker in sneakers:
            for size in sizes:
                if getattr(sneaker.sizes, size, False):
                    tmp.append(sneaker)
                    break
        sneakers = tmp
    response = [SneakersSerializer(x).data for x in sneakers]
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_brands(request):
    brands = Brand.objects.all()
    filter_brand = []
    for brand in brands:
        if Sneaker.objects.filter(brand=brand).exists():
            filter_brand.append(brand.title)
    return Response(filter_brand, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_colors(request):
    sneakers = Sneaker.objects.all()
    filter_color = []
    for sneaker in sneakers:
        if sneaker.color not in filter_color:
            filter_color.append(sneaker.color)
    return Response(filter_color, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_sizes(request):
    sneakers = Sneaker.objects.all()
    filter_size = []
    fields = ['size_350', 'size_355', 'size_360', 'size_365',
              'size_370', 'size_375', 'size_380', 'size_385',
              'size_390', 'size_400', 'size_405', 'size_410',
              'size_420', 'size_425', 'size_430', 'size_440',
              'size_445', 'size_450', 'size_460', 'size_465']
    for sneaker in sneakers:
        for field in fields:
            if getattr(sneaker.sizes, field, False) and field[len(field)-3:] not in filter_size:
                filter_size.append(field[len(field)-3:])
    print(filter_size)
    filter_size.sort()
    return Response(filter_size, status=status.HTTP_200_OK)
