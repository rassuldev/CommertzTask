from django_filters import rest_framework as filters

from employee.models import Employee


class EmployeeFilter(filters.FilterSet):
    position = filters.CharFilter(field_name='position__name', lookup_expr='contains')

    class Meta:
        model = Employee
        fields = ['fullname', 'position', 'salary', 'started_work_date', 'head']

