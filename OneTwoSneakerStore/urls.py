from rest_framework import routers
from .api import *
from .views import *
from django.urls import path

router = routers.DefaultRouter()
# router.register('api/sneakers', SneakersViewSet, 'Sneakers')
router.register('api/orderlist', OrderListViewSet, 'OrderList')

urlpatterns = [
    path('api/addorder', add_order),
    path('api/check', check_server),
    path('api/sneakers/filter', filter_sneakers),
    path('api/filters/brands', get_brands),
    path('api/filters/colors', get_colors),
    path('api/filters/sizes', get_sizes),
] + router.urls
