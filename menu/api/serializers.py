from dataclasses import fields
from pyexpat import model
from rest_framework import serializers 
from menu.models import Item, Menu, MenuItem




class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','name', 'description', 'price', 'restaurant', 'user')





class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'publish_date', 'restaurant', 'user')





class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id','item', 'menu', 'publish_date', 'restaurant', 'user')