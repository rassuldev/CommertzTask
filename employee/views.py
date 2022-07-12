from django.shortcuts import render
from employee.serializers import EmployeeSerializer
from employee.models import Employee
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from employee.filters import EmployeeFilter
from rest_framework.permissions import IsAuthenticated

#For Employee
class EmployeeRetrieveView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#employee list
class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.DjangoFilterBackend, rest_framework_filters.SearchFilter,
                       rest_framework_filters.OrderingFilter]
    search_fields = ['fullname', 'position__name', 'salary', 'started_work_date']
    filterset_class = EmployeeFilter
    permission_classes = [IsAuthenticated]
