from django.db import models


class EmailContacts(models.Model):
    group_id = models.PositiveIntegerField(null=True, blank=True)
    business_unit_id = models.PositiveIntegerField(null=True, blank=True)
    groupEmail = models.CharField(max_length=50)
    isactive = models.BooleanField(default=True)
    createdBy = models.PositiveIntegerField(null=True, blank=True)
    modifiedBy = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'email_contacts'

class EmailGroups(models.Model):
    group_name = models.CharField(max_length=100)
    group_code = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    isactive = models.BooleanField(default=True)
    createdby = models.PositiveIntegerField(null=True, blank=True)
    modifiedby = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'email_groups'

class EmailLogs(models.Model):
    fromEmail = models.CharField(max_length=200, null=True, blank=True)
    toEmail = models.CharField(max_length=200, null=True, blank=True)
    toName = models.CharField(max_length=200, null=True, blank=True)
    cc = models.TextField(null=True, blank=True)
    bcc = models.TextField(null=True, blank=True)
    emailsubject = models.CharField(max_length=255, null=True, blank=True)
    header = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    is_sent = models.BooleanField(default=False)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)
    key1 = models.CharField(max_length=50, null=True, blank=True)
    key2 = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'email_logs'