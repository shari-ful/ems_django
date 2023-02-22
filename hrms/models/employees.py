from django.db import models
from .departments import Department
from .business_unit import Businessunit


departments = Department.objects.all()
MANAGER = [(department.manager, department.manager) for department in departments]

class Employee(models.Model):
    name = models.CharField(max_length=200, null=False)
    employee_id = models.CharField(max_length=100, null=False)
    designation = models.CharField(max_length=100, null=True)
    Role = models.CharField(max_length=100, null=False)
    b_unit = models.CharField(max_length=100, null=False)
    department = models.ForeignKey(Department, to_field='name', on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=False)    
    reporting_manager = models.CharField(max_length=100, choices=MANAGER, null=False)
    date_of_joining = models.DateField(null=True)

    def __str__(self):
        return f'{self.first_name}'