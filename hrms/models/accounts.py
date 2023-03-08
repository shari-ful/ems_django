from django.db import models
from django.contrib.auth.models import User

class AccountClassType(models.Model):
    accountclasstype = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'account_class_type'


class AllottedLeavesLog(models.Model):
    userid = models.BigIntegerField(null=True)
    assignedleaves = models.IntegerField(null=True)
    totalleaves = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    createdby = models.BigIntegerField(null=True)
    modifiedby = models.BigIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'allotted_leaves_log'


class Announcement(models.Model):
    businessunit_id = models.TextField()
    department_id = models.TextField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    attachments = models.TextField()
    status = models.IntegerField(choices=[(1, 'Save as draft'), (2, 'Posted')], null=True)
    isactive = models.BooleanField(null=True)
    createdby = models.BigIntegerField(null=True)
    createdby_role = models.BigIntegerField(null=True)
    createdby_group = models.BigIntegerField(null=True)
    modifiedby = models.BigIntegerField(null=True)
    modifiedby_role = models.BigIntegerField(null=True)
    modifiedby_group = models.BigIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)

    class Meta:
        db_table = 'announcements'

class AssignmentEntryReasonCode(models.Model):
    assignmententryreasoncode = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    createdby = models.PositiveIntegerField(null=True, blank=True)
    modifiedby = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'assignment_entry_reason_code'

class AttendanceStatusCode(models.Model):
    attendancestatuscode = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'attandance_status'

class BankAccountType(models.Model):
    bankaccounttype = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'bank_account_type'



