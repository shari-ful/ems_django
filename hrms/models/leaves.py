from django.db import models

class EmployeeLeave(models.Model):
    user_id = models.BigIntegerField(null=True)
    emp_leave_limit = models.FloatField(null=True)
    used_leaves = models.FloatField(null=True)
    alloted_year = models.PositiveSmallIntegerField(null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)
    isleavetrasnferset = models.BooleanField(default=False)

    class Meta:
        db_table = 'main_employeeleaves'
        unique_together = [('user_id', 'alloted_year')]


