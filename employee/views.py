from django.shortcuts import render
from rest_framework import viewsets 
from .models import Employee
from employee.api.serializers import EmployeeSerializer




class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer