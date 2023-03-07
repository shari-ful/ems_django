from django.db import models
from .employees import Employee

class Department(models.Model):
    deptname = models.CharField(max_length=150)
    deptcode = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    country = models.PositiveIntegerField(null=True, blank=True)
    state = models.PositiveIntegerField(null=True, blank=True)
    city = models.PositiveIntegerField(null=True, blank=True)
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    address3 = models.TextField(null=True, blank=True)
    timezone = models.IntegerField(null=True, blank=True)
    depthead = models.PositiveIntegerField(null=True, blank=True)
    unitid = models.PositiveIntegerField(null=True, blank=True)
    createdby = models.PositiveIntegerField(null=True, blank=True)
    modifiedby = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=True)
    

    def __str__(self):
        return f'{self.deptname}'
    
class DisciplinaryHistory(models.Model):
    incident_id = models.BigIntegerField(null=True)
    description = models.CharField(max_length=300, null=True)
    action_emp_id = models.BigIntegerField(null=True)
    createdby = models.BigIntegerField(null=True)
    createddate = models.DateTimeField(null=True)

    class Meta:
        db_table = 'disciplinary_history'
        managed = False

class DisciplinaryIncident(models.Model):
    incident_raised_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='reported_incidents')
    employee_bu = models.ForeignKey('EmployeeBU', on_delete=models.SET_NULL, null=True, related_name='disciplinary_incidents')
    employee_dept = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name='disciplinary_incidents')
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='disciplinary_incidents')
    employee_rep_mang = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='represented_incidents')
    date_of_occurrence = models.DateField(null=True)
    violation = models.ForeignKey('Violation', on_delete=models.SET_NULL, null=True, related_name='disciplinary_incidents')
    violation_expiry = models.DateField(null=True)
    employee_job_title = models.ForeignKey('JobTitle', on_delete=models.SET_NULL, null=True, related_name='disciplinary_incidents')
    employer_statement = models.TextField(null=True)
    employee_appeal = models.BooleanField(default=True)
    employee_statement = models.TextField(null=True)
    cao_verdict = models.BooleanField(default=True)
    corrective_action = models.CharField(max_length=50, choices=[('Suspension With Pay', 'Suspension With Pay'), ('Suspension W/O Pay', 'Suspension W/O Pay'), ('Termination', 'Termination'), ('Other', 'Other')])
    corrective_action_text = models.CharField(max_length=255, null=True)
    incident_status = models.CharField(max_length=50, choices=[('Initiated', 'Initiated'), ('Appealed', 'Appealed'), ('Closed', 'Closed')], default='Initiated')
    created_by = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='created_incidents')
    modified_by = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='modified_incidents')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'disciplinary_incident'

class MainDisciplinaryViolationType(models.Model):
    violationname = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    createdby = models.PositiveIntegerField(null=True, blank=True)
    modifiedby = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'disciplinary_violation_types'