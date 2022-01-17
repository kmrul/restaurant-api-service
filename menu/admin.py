import imp
from django.contrib import admin
from .models import Item, MenuItem

admin.site.register(Item)
admin.site.register(MenuItem)
