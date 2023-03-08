from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    employee_id = models.BigIntegerField(null=True)
    employee_name = models.CharField(max_length=200, null=False)
    date_of_joining = models.DateField(default='0000-00-00')
    date_of_leaving = models.DateField(default='0000-00-00')
    reporting_manager = models.TextChoices()
    emp_status_id = models.PositiveIntegerField(null=True)
    businessunit_id = models.PositiveIntegerField(null=True)
    department_id = models.PositiveIntegerField(null=True)
    jobtitle_id = models.PositiveIntegerField(null=True)
    position_id = models.PositiveIntegerField(null=True)
    years_exp = models.CharField(max_length=20, null=True)
    holiday_group = models.PositiveIntegerField(null=True)
    prefix_id = models.PositiveIntegerField(null=True)
    extension_number = models.CharField(max_length=20, null=True)
    office_number = models.CharField(max_length=100, null=True)
    office_faxnumber = models.CharField(max_length=100, null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)
    is_orghead = models.BooleanField(default=False)

    class Meta:
        db_table = 'employees'

    
class MainEducationLevelCode(models.Model):
    educationlevelcode = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    createdby = models.PositiveIntegerField(null=True, blank=True)
    modifiedby = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'education_level_code'

class MainEEOCCategory(models.Model):
    eeoccategory = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    createdby = models.PositiveIntegerField(null=True, blank=True)
    modifiedby = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'eeoccategory'


class EmployeeReporting(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reporting_manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'emp_reporting'


class EmpAdditionalDetails(models.Model):
    user_id = models.BigIntegerField(null=True)
    military_status = models.BooleanField(null=True)
    countries_served = models.PositiveIntegerField(null=True)
    branch_service = models.CharField(max_length=100, null=True)
    rank_achieved = models.CharField(max_length=100, null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    special_training = models.TextField(null=True)
    awards = models.TextField(null=True)
    discharge_status = models.BooleanField(null=True)
    service_number = models.CharField(max_length=100, null=True)
    rank = models.CharField(max_length=100, null=True)
    verification_report = models.CharField(max_length=100, null=True)
    military_servicetype = models.PositiveIntegerField(null=True)
    veteran_status = models.PositiveIntegerField(null=True)
    createdby = models.PositiveBigIntegerField(null=True)
    modifiedby = models.PositiveBigIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'empadditional_details'

class EmpCertificationDetails(models.Model):
    user_id = models.BigIntegerField(null=True)
    course_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    course_level = models.CharField(max_length=100, null=True)
    course_offered_by = models.CharField(max_length=100, null=True)
    certification_name = models.CharField(max_length=100, null=True)
    issued_date = models.DateField(null=True)
    createdby = models.PositiveBigIntegerField(null=True)
    modifiedby = models.PositiveBigIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'empcertification_details'
        verbose_name_plural = 'Employee Certification Details'

class EmpCommunicationDetails(models.Model):
    user_id = models.BigIntegerField(null=True)
    personalemail = models.CharField(max_length=100, null=True)
    perm_streetaddress = models.CharField(max_length=200, null=True)
    perm_country = models.BigIntegerField(null=True)
    perm_state = models.BigIntegerField(null=True)
    perm_city = models.BigIntegerField(null=True)
    perm_pincode = models.CharField(max_length=15, null=True)
    current_streetaddress = models.CharField(max_length=200, null=True)
    current_country = models.BigIntegerField(null=True)
    current_state = models.BigIntegerField(null=True)
    current_city = models.BigIntegerField(null=True)
    current_pincode = models.CharField(max_length=15, null=True)
    emergency_number = models.CharField(max_length=100, null=True)
    emergency_name = models.CharField(max_length=50, null=True)
    emergency_email = models.CharField(max_length=100, null=True)
    createdby = models.PositiveBigIntegerField(null=True)
    modifiedby = models.PositiveBigIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'empcommunication_details'
        verbose_name_plural = 'Employee Communication Details'

class EmpDependencyDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dependent_name = models.CharField(max_length=100, null=True)
    dependent_relation = models.CharField(max_length=100, null=True)
    dependent_custody = models.CharField(max_length=100, null=True)
    dependent_dob = models.DateField(null=True)
    dependent_age = models.PositiveIntegerField(null=True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    modifiedby = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createddate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'empdependency_details'

class EmpDisabilityDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disability_name = models.CharField(max_length=50, null=True)
    disability_type = models.CharField(max_length=100, null=True)
    other_disability_type = models.CharField(max_length=100, null=True)
    disability_description = models.TextField(null=True)
    createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    modifiedby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'empdisability_details'

class EmpEducationDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    educationlevel = models.PositiveIntegerField(null=True)
    institution_name = models.CharField(max_length=255, null=True)
    course = models.CharField(max_length=100, null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    percentage = models.PositiveIntegerField(null=True)
    createdby = models.PositiveBigIntegerField(null=True)
    modifiedby = models.PositiveBigIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'empeducation_details'

class EmpExperianceDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=100)
    comp_website = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    reason_for_leaving = models.TextField()
    reference_name = models.CharField(max_length=100)
    reference_contact = models.CharField(max_length=100)
    reference_email = models.CharField(max_length=100)
    createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    modifiedby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createddate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'empexperiance_details'

class EmpHoliday(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    holiday_group_id = models.PositiveIntegerField(null=True, blank=True)
    createdby = models.PositiveBigIntegerField(null=True, blank=True)
    modifiedby = models.PositiveBigIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'emp_holidays'

class EmpJobHistory(models.Model):
    user_id = models.BigIntegerField(null=True)
    positionheld = models.PositiveIntegerField(null=True)
    department = models.PositiveIntegerField(null=True)
    jobtitleid = models.PositiveIntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    active_company = models.BooleanField(null=True)
    client_id = models.PositiveIntegerField(null=True)
    vendor = models.CharField(max_length=200, null=True)
    paid_amount = models.DecimalField(max_digits=25, decimal_places=2, null=True)
    received_amount = models.DecimalField(max_digits=25, decimal_places=2, null=True)
    createdby = models.BigIntegerField(null=True)
    modifiedby = models.BigIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(null=True)

    class Meta:
        db_table = 'empjob_history'

class EmployeeDocuments(models.Model):
    user_id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    attachments = models.TextField(null=True)
    createdby = models.BigIntegerField(null=True)
    modifiedby = models.BigIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'employee_documents'


class EmployeeLeaveType(models.Model):
    leavetype = models.CharField(max_length=255, null=True)
    numberofdays = models.PositiveIntegerField(null=True)
    leavecode = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    leavepreallocated = models.BooleanField(null=True, default=False)
    leavepredeductable = models.BooleanField(null=True, default=False)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'main_employeeleavetypes'

class EmploymentStatus(models.Model):
    workcode = models.CharField(max_length=255, null=True)
    workcodename = models.PositiveIntegerField(null=True)
    default_leaves = models.IntegerField(default=0)
    description = models.CharField(max_length=255, null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'main_employmentstatus'

class EmployeeSummery(models.Model):
    user_id = models.PositiveIntegerField(null=True)
    date_of_joining = models.DateField(null=True)
    date_of_leaving = models.DateField(null=True)
    reporting_manager = models.PositiveIntegerField(null=True)
    reporting_manager_name = models.CharField(max_length=250, null=True)
    emp_status = models.ForeignKey(EmploymentStatus, on_delete=models.SET_NULL, null=True)
    businessunit_id = models.PositiveIntegerField(null=True)
    businessunit_name = models.CharField(max_length=250, null=True)
    department_id = models.PositiveIntegerField(null=True)
    department_name = models.CharField(max_length=250, null=True)
    jobtitle_id = models.PositiveIntegerField(null=True)
    jobtitle_name = models.CharField(max_length=250, null=True)
    position_id = models.PositiveIntegerField(null=True)
    position_name = models.CharField(max_length=250, null=True)
    years_exp = models.CharField(max_length=10, null=True)
    holiday_group = models.PositiveIntegerField(null=True)
    holiday_group_name = models.CharField(max_length=250, null=True)
    prefix_id = models.PositiveIntegerField(null=True)
    prefix_name = models.CharField(max_length=250, null=True)
    extension_number = models.CharField(max_length=20, null=True)
    office_number = models.CharField(max_length=20, null=True)
    office_faxnumber = models.CharField(max_length=20, null=True)
    emprole = models.PositiveIntegerField(null=True)
    emprole_name = models.CharField(max_length=250, null=True)
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    userfullname = models.CharField(max_length=250, null=True)
    emailaddress = models.CharField(max_length=100, null=True)
    contactnumber = models.CharField(max_length=20, null=True)
    backgroundchk_status = models.CharField(max_length=20, null=True, choices=[('In process', 'In process'), ('Completed', 'Completed'), ('Not Applicable', 'Not Applicable'), ('Yet to start', 'Yet to start'), ('On hold', 'On hold')])
    employeeId = models.CharField(max_length=20, null=True)
    modeofentry = models.CharField(max_length=100, null=True)
    other_modeofentry = models.CharField(max_length=100, null=True)
    selecteddate = models.DateField(null=True)
    candidatereferredby = models.PositiveIntegerField(null=True)
    referer_name = models.CharField(max_length=250, null=True)
    profileimg = models.CharField(max_length=250, null=True)
    createdby = models.PositiveIntegerField(null=True)
    createdby_name = models.CharField(max_length=250, null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
