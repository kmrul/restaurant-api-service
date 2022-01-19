from base.models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework import viewsets

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
