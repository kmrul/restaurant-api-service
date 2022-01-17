from base.api.viewsets import RestaurantViewSet
from auth.api.viewsets import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('restaurant', RestaurantViewSet)

router.register('user', UserViewSet)