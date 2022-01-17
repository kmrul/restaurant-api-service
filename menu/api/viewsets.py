from menu.models import Item, MenuItem
from .serializers import ItemSerializer, MenuItemSerializer
from rest_framework import viewsets


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItem

    