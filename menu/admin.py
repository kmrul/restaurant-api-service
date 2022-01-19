import imp
from django.contrib import admin
from .models import Item, Menu, MenuItem

admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(MenuItem)
