from django.contrib import admin
from .models import MonthlyExpenseModel, Assets, BudgetReview

# Adds BlogPost model to admin site
admin.site.register(MonthlyExpenseModel)
admin.site.register(Assets)
admin.site.register(BudgetReview)
# Register your models here.