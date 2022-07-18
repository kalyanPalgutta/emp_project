from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Details(models.Model):
    EmployeeId = models.CharField(max_length=200, null=True)
    EmployeeName = models.CharField(max_length=50, null=True)
    Designation = models.CharField(max_length=50, null=True)
    JoinedDate = models.DateField()
    Address = models.CharField(max_length=100, null=True)
    Phone = models.IntegerField(null=True)
    EMail = models.CharField(max_length=50, null=True)
    Salary = models.IntegerField(default=0)
    WorkingDays = models.IntegerField(default=0)

    def __str__(self):
        return self.EmployeeName