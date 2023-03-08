from django.db import models
from django.contrib.auth.models import User


class BgAgencyList(models.Model):
    user_id = models.PositiveIntegerField(null=True, blank=True)
    agencyname = models.CharField(max_length=255)
    primaryphone = models.CharField(max_length=100)
    secondaryphone = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bg_checktype = models.CharField(max_length=255)
    website_url = models.URLField(null=True, blank=True)
    flag = models.BooleanField(default=True)
    createdby = models.PositiveIntegerField(null=True, blank=True)
    modifiedby = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.agencyname

    class Meta:
        db_table = 'bg_agencylist'

class BgCheckDetails(models.Model):
    specimen_id = models.IntegerField(null=True)
    flag = models.BooleanField(default=True, help_text='1 - employee, 2- candidate')
    process_status = models.CharField(max_length=20, default='In process', choices=[('In process', 'In process'), ('On hold', 'On hold'), ('Complete', 'Complete')])
    bgagency_id = models.IntegerField(null=True)
    bgcheck_type = models.CharField(max_length=100, null=True)
    bgagency_pocid = models.IntegerField(null=True)
    bgcheck_status = models.CharField(max_length=20, default='In process', choices=[('Yet to start', 'Yet to start'), ('In process', 'In process'), ('On hold', 'On hold'), ('Complete', 'Complete')])
    explanation = models.TextField(null=True)
    feedback_file = models.CharField(max_length=50, null=True)
    feedback_deletedby = models.IntegerField(null=True)
    createdby = models.IntegerField(null=True)
    modifiedby = models.IntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True, help_text='0 - Process deleted, 1 - Active, 2 - Agency deleted')
    recentlycommentedby = models.IntegerField(null=True)
    recentlycommenteddate = models.DateTimeField(null=True)

    class Meta:
        db_table = 'bg_checkdetails'
class BGCheckComments(models.Model):
    bgdet = models.ForeignKey(BgCheckDetails, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    createddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'bg_checkcomments'


class BgChecksSummary(models.Model):
    detail_id = models.BigIntegerField(null=True)
    specimen_name = models.CharField(max_length=200, null=True)
    specimen_id = models.BigIntegerField(null=True)
    specimen_flag = models.BooleanField(default=True)
    specimen_flag_name = models.CharField(max_length=10, choices=[('Employee', 'Employee'), ('Candidate', 'Candidate')], default='Employee')
    employee_id = models.CharField(max_length=200, null=True)
    screeningtypeid = models.BigIntegerField(null=True)
    screeningtype_name = models.CharField(max_length=200, null=True)
    agencyid = models.BigIntegerField(null=True)
    agencyname = models.CharField(max_length=200, null=True)
    process_status = models.CharField(max_length=20, choices=[('In process', 'In process'), ('On hold', 'On hold'), ('Complete', 'Complete')], default='In process')
    month_name = models.CharField(max_length=200, null=True)
    year_year = models.CharField(max_length=4, null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    createdby = models.BigIntegerField(null=True)
    createdname = models.CharField(max_length=200, null=True)
    modifiedby = models.BigIntegerField(null=True)
    modifiedname = models.CharField(max_length=200, null=True)
    isactive = models.BooleanField(default=True)
    isactive_text = models.CharField(max_length=50, default='Active')

    class Meta:
        db_table = 'bg_checkssummary'

class BgCheckType(models.Model):
    type = models.CharField(max_length=150)
    description = models.TextField(null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'bg_checktype'

class BgPocDetails(models.Model):
    bg_agencyid = models.PositiveIntegerField(null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    contact_no = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=150, null=True)
    location = models.CharField(max_length=200, null=True)
    city = models.PositiveIntegerField(null=True)
    state = models.PositiveIntegerField(null=True)
    country = models.PositiveIntegerField(null=True)
    contact_type = models.BooleanField(default=True, verbose_name='contact type') # True is primary and False is secondary
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'bg_pocdetails'