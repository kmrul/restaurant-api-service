from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Item, MenuItem, Menu
from menu.api.serializers import ItemSerializer, MenuSerializer, MenuItemSerializer




class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer




class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


    def get(self, request, *args, **kwargs):
        print("get data 123")
        return self.retrieve(request, *args, **kwargs)



    def create(self, request, *args, **kwargs):
        each_day_menu = list(Menu.objects.filter(publish_date=request.data.get('publish_date')))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if len(each_day_menu) > 0:
            return Response("This day menu already added.", status=status.HTTP_400_BAD_REQUEST,)
        
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
    def retrieve_each_day_menu(self, request, pk=None):
        queryset = Menu.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = MenuSerializer(user)
        return Response(serializer.data)

    


class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer