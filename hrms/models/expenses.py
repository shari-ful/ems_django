from django.db import models


class ExpenseAdvance(models.Model):
    TYPE_CHOICES = [
        ('advance', 'Advance'),
        ('return', 'Return')
    ]
    
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default='advance')
    from_id = models.IntegerField(null=True)
    to_id = models.IntegerField(null=True)
    payment_ref_number = models.CharField(max_length=200, null=True)
    payment_mode_id = models.IntegerField(null=True)
    project_id = models.IntegerField(null=True)
    currency_id = models.IntegerField(null=True)
    amount = models.FloatField(null=True)
    application_currency_id = models.IntegerField(null=True)
    application_amount = models.FloatField(null=True)
    advance_conversion_rate = models.FloatField(null=True)
    description = models.TextField(null=True)
    createdby = models.IntegerField(null=True)
    modifiedby = models.IntegerField(null=True)
    createddate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'expense_advance'

class ExpenseForward(models.Model):
    expense_id = models.IntegerField(null=True)
    trip_id = models.IntegerField(null=True)
    from_id = models.IntegerField(null=True)
    to_id = models.IntegerField(null=True)
    createdby = models.IntegerField(null=True)
    modifiedby = models.IntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'expense_forward'

class ExpenseHistory(models.Model):
    expense_id = models.IntegerField(null=True)
    trip_id = models.IntegerField(null=True)
    history = models.CharField(max_length=500, null=True)
    createdby = models.IntegerField(null=True)
    modifiedby = models.IntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'expense_history'

class ExpenseNotifications(models.Model):
    expense_id = models.IntegerField(null=True)
    trip_id = models.IntegerField(null=True)
    notification = models.CharField(max_length=500, null=True)
    link = models.CharField(max_length=200, null=True)
    createdby = models.IntegerField(null=True)
    modifiedby = models.IntegerField(null=True)
    createddate = models.DateTimeField(null=True)
    modifieddate = models.DateTimeField(null=True)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'expense_notifications'


# class Expense(models.Model):
#     SAVED = 'saved'
#     SUBMITTED = 'submitted'
#     APPROVED = 'approved'
#     REJECTED = 'rejected'
#     EXPENSE_STATUSES = [
#         (SAVED, 'Saved'),
#         (SUBMITTED, 'Submitted'),
#         (APPROVED, 'Approved'),
#         (REJECTED, 'Rejected'),
#     ]

#     expense_name = models.CharField(max_length=100, null=True)
#     category = models.ForeignKey('ExpenseCategory', on_delete=models.SET_NULL, null=True)
#     project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
#     client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
#     trip = models.ForeignKey('Trip', on_delete=models.SET_NULL, null=True)
#     manager = models.ForeignKey('Manager', on_delete=models.SET_NULL, null=True)
#     expense_date = models.DateField(null=True)
#     expense_currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, related_name='expense_currency', null=True)
#     expense_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     expense_conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
#     application_currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, related_name='application_currency', null=True)
#     application_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     advance_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     is_reimbursable = models.BooleanField(null=True)
#     is_from_advance = models.BooleanField(default=False)
#     expense_payment = models.ForeignKey('ExpensePaymentMethod', on_delete=models.SET_NULL, null=True)
#     expense_payment_ref_no = models.CharField(max_length=200, null=True)
#     description = models.TextField(null=True)
#     status = models.CharField(max_length=20, choices=EXPENSE_STATUSES, default=SAVED)
#     createdby = models.IntegerField(null=True)
#     modifiedby = models.IntegerField(null=True)
#     createddate = models.DateTimeField(null=True)
#     modifieddate = models.DateTimeField(null=True)
#     isactive = models.BooleanField(null=True)

#     def __str__(self):
#         return f'{self.expense_name} - {self.expense_amount}'