from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=False)
    street_adress_1 = models.TextField(max_length=500, null=True)
    street_adress_2 = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.name}'

class Businessunit(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    code = models.CharField(max_length=20, null=True)
    category = models.CharField(max_length=20, null=True)
    company = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=500, null=True)
    started_on = models.DateField()
    country = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=False)
    street_adress_1 = models.TextField(max_length=500, null=True)
    street_adress_2 = models.TextField(max_length=500, null=True)

    REQUIRED_FIELDS = ['name', 'company', 'country']

    def __str__(self):
        return f'{self.name}'