import imp
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('item', views.ItemView)
router.register('menu-item', views.MenuItemView)
router.register('menu-card', views.MenuView)

urlpatterns = [
    path('', include(router.urls))
]