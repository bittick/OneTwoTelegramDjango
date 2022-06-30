from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/sneakers', SneakersViewSet, 'Sneakers')

urlpatterns = router.urls
