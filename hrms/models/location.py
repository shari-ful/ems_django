from django.db import models


class City(models.Model):
    country = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=300, null=True)
    name = models.CharField(max_length=255)
    city_org_id = models.PositiveIntegerField()
    created_by = models.CharField(max_length=300, null=True)
    modified_by = models.CharField(max_length=300, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('state', 'city_org_id')

    def __str__(self):
        return self.name
    

class CompetenceLevel(models.Model):
    competencylevel = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'main_competencylevel'

class Country(models.Model):
    country = models.CharField(max_length=255)
    countrycode = models.CharField(max_length=255, null=True)
    citizenship = models.CharField(max_length=255, null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)
    country_id_org = models.PositiveIntegerField(null=True)

class CronStatus(models.Model):
    GENERAL = 'General'
    EMPLOYEE_EXPIRY = 'Employee expiry'
    REQUISITION_EXPIRY = 'Requisition expiry'
    APPROVE_LEAVE = 'Approve leave'
    INACTIVE_USERS = 'Inactive users'
    EMP_DOCS_EXPIRY = 'Emp docs expiry'

    CRON_TYPE_CHOICES = [
        (GENERAL, 'General'),
        (EMPLOYEE_EXPIRY, 'Employee expiry'),
        (REQUISITION_EXPIRY, 'Requisition expiry'),
        (APPROVE_LEAVE, 'Approve leave'),
        (INACTIVE_USERS, 'Inactive users'),
        (EMP_DOCS_EXPIRY, 'Emp docs expiry'),
    ]

    cron_type = models.CharField(
        max_length=20,
        choices=CRON_TYPE_CHOICES,
        default=GENERAL,
    )
    cron_status = models.IntegerField(null=True)
    started_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'main_cronstatus'


class Currency(models.Model):
    currencyname = models.CharField(max_length=255)
    currencycode = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    createdby = models.PositiveIntegerField(null=True, blank=True)
    modifiedby = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)
    isactive = models.BooleanField(default=True)

class CurrencyConverter(models.Model):
    basecurrency = models.IntegerField(null=True)
    targetcurrency = models.IntegerField(null=True)
    basecurrtext = models.CharField(max_length=255, null=True)
    targetcurrtext = models.CharField(max_length=255, null=True)
    exchangerate = models.CharField(max_length=255, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    createdby = models.IntegerField(null=True)
    description = models.CharField(max_length=255, null=True)
    modifiedby = models.IntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

class DateFormat(models.Model):
    mysql_dateformat = models.CharField(max_length=50, null=True, verbose_name='format for mysql')
    js_dateformat = models.CharField(max_length=50, null=True, verbose_name='format for javascript')
    dateformat = models.CharField(max_length=50, verbose_name='for php')
    example = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=255, null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'main_dateformat'
        verbose_name_plural = 'Date Formats'

    def __str__(self):
        return self.dateformat