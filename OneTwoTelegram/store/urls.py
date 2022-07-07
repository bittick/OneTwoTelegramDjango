from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/sneakers', SneakersViewSet, 'Sneakers')
router.register('api/orderlist', OrderListViewSet, 'OrderList')

urlpatterns = router.urls
