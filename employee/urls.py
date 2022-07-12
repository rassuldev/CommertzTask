from django.contrib import admin
from django.urls import path
from employee.views import EmployeeRetrieveView, EmployeeListView
app_name = 'employee'
urlpatterns = [
    path('<int:pk>/', EmployeeRetrieveView.as_view()),
    path('', EmployeeListView.as_view()),
]