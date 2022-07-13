from rest_framework import routers
from .api import *
from django.urls import path

router = routers.DefaultRouter()
router.register('api2/vegetables', VegetablesViewSet, 'Vegetables')
router.register('api2/customers', CustomersViewSet, 'Customers')

urlpatterns = [
    path('api2/addcustomer', add_customer),
    path('api2/addorder', add_order),
] + router.urls
