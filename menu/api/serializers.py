from dataclasses import fields
from pyexpat import model
from rest_framework import serializers 
from menu.models import Item, MenuItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price')


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('item', 'publish_date')