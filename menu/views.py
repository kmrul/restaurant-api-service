import imp
from django.shortcuts import render
from rest_framework import viewsets 
from .models import Item, MenuItem
from menu.api.serializers import ItemSerializer, MenuItemSerializer

class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer