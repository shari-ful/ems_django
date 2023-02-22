from django.db import models


class AssetsCategory(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.CharField(max_length=11, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'assets_categories'

class Assets(models.Model):
    category = models.IntegerField(null=True, blank=True)
    sub_category = models.IntegerField(null=True, blank=True)
    company_asset_code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=15)
    allocated_to = models.IntegerField(null=True, blank=True)
    responsible_technician = models.IntegerField(null=True, blank=True)
    vendor = models.IntegerField(null=True, blank=True)
    asset_classification = models.CharField(max_length=50)
    purchase_date = models.DateField(null=True, blank=True)
    invoice_number = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=50)
    key_number = models.CharField(max_length=11)
    warenty_status = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    warenty_end_date = models.DateField(null=True, blank=True)
    is_working = models.CharField(max_length=3, choices=[('No', 'No'), ('Yes', 'Yes')])
    notes = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    imagencrpname = models.TextField()
    qr_image = models.TextField()
    isactive = models.BooleanField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'assets'

class AssetsHistory(models.Model):
    asset_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    history = models.CharField(max_length=500, null=True, blank=True)
    isactive = models.BooleanField(null=True, blank=True)
    createdby = models.IntegerField(null=True, blank=True)
    modifiedby = models.IntegerField(null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    modifieddate = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'assets_history'

