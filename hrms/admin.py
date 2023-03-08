from django.contrib import admin
from django.contrib.auth.models import Group
from .models.business_unit import Company, BusinessUnit
from .models.employees import Employee
from .models.departments import Department
from .models.expenses import Expense
from .models.assets import Assets, AssetsCategory
# from .models.expenses import Expense

# Register your models here.

admin.site.site_header = 'EMS Django Project'


# class BunitAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'category', 'company', 'started_on')
    

# class DeptAdmin(admin.ModelAdmin):
#     list_display = ('name', 'b_unit', 'head_of_department', 'manager')

# class EmpAdmin(admin.ModelAdmin):
#     list_display = ('name', 'department', 'reporting_manager')

admin.site.register(Company)
admin.site.register(BusinessUnit)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Assets)
admin.site.register(AssetsCategory)
admin.site.register(Expense)


