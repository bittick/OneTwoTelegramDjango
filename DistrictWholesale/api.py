from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json


class VegetablesViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get']
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VegetableSerializer


class CustomersViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        telegram_id = self.request.query_params.get('tg_id')

        if telegram_id is not None:
            queryset = queryset.filter(telegram_id=telegram_id)
        else:
            queryset = None

        return queryset


@api_view(['POST'])
def filter_products(request):
    filter_data = json.loads(request.body)
    keys = list(filter_data.keys())
    kwargs = {}
    if 'category' in keys:
        categories = []
        for cat in filter_data['category']:
            categories.append(Category.objects.get(title=cat))
        kwargs['product_cat__in'] = categories
    products = Product.objects.filter(**kwargs)
    response = [VegetableSerializer(x, context={'request': request}).data for x in products]
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_order(request):
    order_info = json.loads(request.body.decode("utf-8"))
    current_customer = Customer.objects.get(telegram_id=order_info['customer_tg_id'])
    print(type(order_info), order_info)
    order = OrderList(
        customer=current_customer,
        shipping_address=order_info['shipping_address'],
        comment=order_info['comment'],
        is_paid=False,
        delivery_required=order_info['delivery_required']
    )
    for item in order_info['order_items']:
        if not Product.objects.filter(id=item['vegetable_id']).exists():
            return Response({'e': 'No such vegetable_id'}, status.HTTP_400_BAD_REQUEST)
    order.save()
    for item in order_info['order_items']:
        print(item['vegetable_id'])
        vegetable = Product.objects.get(id=item['vegetable_id'])
        cur_item = OrderItem(
            order_id=order,
            product_id=vegetable,
            quantity=item['quantity']
        )
        cur_item.save()
    return Response({'order_id': order.id}, status.HTTP_200_OK)


@api_view(['POST'])
def add_customer(request):
    customer_info = json.loads(request.body.decode("utf-8"))
    customer = Customer(
        name=customer_info['name'],
        telegram_id=customer_info['tg_id'],
        phone_number=customer_info['phone_number'],
    )
    customer.save()
    return Response({'customer_id': customer.id}, status.HTTP_200_OK)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    filter_category = []
    for category in categories:
        if Product.objects.filter(product_cat=category).exists():
            filter_category.append(category.title)
    return Response(filter_category, status=status.HTTP_200_OK)
