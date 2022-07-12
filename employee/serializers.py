from rest_framework import serializers
from employee.models import Employee, Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['name']


class HeadEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'fullname']


class EmployeeSerializer(serializers.ModelSerializer):
    head = HeadEmployeeSerializer()
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'fullname', 'position', 'salary', 'started_work_date', 'head']
