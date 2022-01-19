import imp
from urllib.error import HTTPError
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Item, MenuItem, Menu
from menu.api.serializers import ItemSerializer, MenuSerializer, MenuItemSerializer

class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def create(self, request, *args, **kwargs):
        each_day_menu = list(Menu.objects.filter(publish_date=request.data.get('publish_date')))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if len(each_day_menu) > 0:
            return Response("This day menu already added.", status=status.HTTP_403_FORBIDDEN,)
        
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer