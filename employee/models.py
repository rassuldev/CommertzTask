from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    name = models.CharField(max_length=255)


class Employee(models.Model):
    fullname = models.CharField(max_length=200, null=False)
    position = models.ForeignKey(Position, null=True, on_delete=models.SET_NULL)
    started_work_date = models.DateTimeField(auto_now_add=True) #automatically fill
    salary = models.IntegerField()
    head = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE) #user related to employee

    def __str__(self):
        return self.fullname