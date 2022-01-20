from os import name
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('base.urls'), name='base'),
    path('menu/', include('menu.urls'), name='menu'),
    path('employee/', include('employee.urls'), name='employee'),
    path('vote/', include('vote.urls'), name='vote'),
    path('auth/', include('auth.urls'), name='auth'),
    path('api/', get_schema_view(
        title="Restaurant APIs Service",
        description="API developers hoping to use our service"
    ), name='api-schema'),
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'api-schema'}
    ), name='swagger-ui'),
]
