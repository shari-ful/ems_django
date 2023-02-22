from django.db import models
from .business_unit import Businessunit

class Department(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    b_unit = models.CharField(max_length=20, null=True)
    head_of_department = models.CharField(max_length=20, null=True)
    manager = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.name}'