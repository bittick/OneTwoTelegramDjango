from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/sneakers', SneakersViewSet, 'Sneakers')
router.register('api/sizessneakers', SizesSneakersViewSet, 'SizesSneakers')

urlpatterns = router.urls
