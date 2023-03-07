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


class BusinessUnit(models.Model):
    unitname = models.CharField(max_length=255)
    unitcode = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    country = models.PositiveIntegerField(null=True, blank=True)
    state = models.PositiveIntegerField(null=True, blank=True)
    city = models.PositiveIntegerField(null=True, blank=True)
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    address3 = models.TextField(null=True, blank=True)
    timezone = models.PositiveIntegerField(null=True, blank=True)
    unithead = models.CharField(max_length=255, null=True, blank=True)
    service_desk_flag = models.BooleanField(default=True)
    createdby = models.PositiveIntegerField(null=True, blank=True)
    modifiedby = models.PositiveIntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.unitname
    
class CandidateDetails(models.Model):
    requisition_id = models.IntegerField(null=True)
    candidate_firstname = models.CharField(max_length=50, null=True)
    candidate_lastname = models.CharField(max_length=50, null=True)
    candidate_name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=70, null=True)
    contact_number = models.CharField(max_length=15, null=True)
    profileimg = models.CharField(max_length=100, null=True)
    cand_resume = models.CharField(max_length=100, null=True, db_column='cand_resume', help_text='resume file location')
    cand_resume_deletedby = models.IntegerField(null=True)
    qualification = models.CharField(max_length=100)
    experience = models.FloatField(null=True)
    skillset = models.TextField(null=True)
    education_summary = models.TextField(null=True)
    summary = models.TextField(null=True, help_text='instead of resume')
    CAND_STATUS_CHOICES = [
        ('Shortlisted', 'Shortlisted'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
        ('On hold', 'On hold'),
        ('Disqualified', 'Disqualified'),
        ('Scheduled', 'Scheduled'),
        ('Not Scheduled', 'Not Scheduled'),
        ('Recruited', 'Recruited'),
        ('Requisition Closed/Completed', 'Requisition Closed/Completed'),
    ]
    cand_status = models.CharField(max_length=50, choices=CAND_STATUS_CHOICES)
    BGCHK_STATUS_CHOICES = [
        ('In process', 'In process'),
        ('Completed', 'Completed'),
        ('Not Applicable', 'Not Applicable'),
        ('Yet to start', 'Yet to start'),
        ('On hold', 'On hold'),
    ]
    backgroundchk_status = models.CharField(max_length=50, choices=BGCHK_STATUS_CHOICES, default='Yet to start')
    cand_location = models.CharField(max_length=150, null=True)
    city = models.IntegerField(null=True)
    state = models.IntegerField(null=True)
    country = models.IntegerField(null=True)
    pincode = models.CharField(max_length=15, null=True)
    SOURCE_CHOICES = [
        ('Vendor', 'Vendor'),
        ('Website', 'Website'),
        ('Referal', 'Referal'),
    ]
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, null=True)
    source_val = models.CharField(max_length=150, null=True)
    createdby = models.IntegerField(null=True)
    modifiedby = models.IntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'candidate_details'

class CandWorkDetails(models.Model):
    cand = models.ForeignKey(CandidateDetails, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, null=True)
    contact_number = models.CharField(max_length=20, null=True)
    company_address = models.CharField(max_length=500, null=True)
    company_website = models.CharField(max_length=100, null=True)
    cand_designation = models.CharField(max_length=60, null=True)
    cand_fromdate = models.DateField(null=True)
    cand_todate = models.DateField(null=True)
    createdby = models.PositiveIntegerField(null=True)
    modifiedby = models.PositiveIntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'candwork_details'
    
