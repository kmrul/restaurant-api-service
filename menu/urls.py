import imp
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('item', views.ItemView)
router.register('', views.MenuItemView)

urlpatterns = [
    path('', include(router.urls))
]