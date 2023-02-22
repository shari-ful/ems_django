from django.contrib import admin
from django.contrib.auth.models import Group
from .models.business_unit import Company, Businessunit
from .models.employees import Employee
from .models.departments import Department
from .models.assets import Assets
# from .models.expenses import Expense

# Register your models here.

admin.site.site_header = 'EMS Django Project'


class BunitAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category', 'company', 'started_on')
    

class DeptAdmin(admin.ModelAdmin):
    list_display = ('name', 'b_unit', 'head_of_department', 'manager')

class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'reporting_manager')

admin.site.register(Businessunit, BunitAdmin)
admin.site.register(Department, DeptAdmin)
admin.site.register(Employee, EmpAdmin)
admin.site.register(Assets)

