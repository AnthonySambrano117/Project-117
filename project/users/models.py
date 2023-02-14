from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.


class BaseModel(models.Model):
    username = models.CharField(validators=[MinLengthValidator(11)], max_length=32)
    password = models.CharField(validators=[MinLengthValidator(11)], max_length=32)


# Create a form class that inherits from BaseForm
class RegistrationModel(BaseModel):
    email = models.EmailField()
    password_confirmation = models.CharField(validators=[MinLengthValidator(11)], max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class MonthlyExpenseModel(models.Model):
    amount_cars=models.IntegerField()
    rent_bill=models.IntegerField()
    mortgage_bill=models.IntegerField()
    mortgage_interest_rate=models.IntegerField()
    gorcerys=models.IntegerField()
    dinning_out=models.IntegerField()
    gas=models.IntegerField()
    internet=models.IntegerField()
    phone_bill=models.IntegerField()
    utilites=models.IntegerField()
    miscellaneous=models.IntegerField()
    # user_id = models.ForeignKey(models.IntegerField(), on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class Assets(models.Model):
    income=models.IntegerField()
    savings_amount=models.IntegerField()
    savings_interest_rate=models.IntegerField()
    amount_in_stocks=models.IntegerField()
    yes_no_401K=models.CharField(max_length=3)
    interest_401K_match=models.IntegerField()
    roth_investing=models.IntegerField()
    roth_amount=models.IntegerField()
    pass_miscellaneous=models.IntegerField()
    # user_id = models.ForeignKey(models.IntegerField(), on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    


class BudgetReview(models.Model):
    Total_Monthly_Savings=models.IntegerField()
    Total_Monthly_Expenses=models.IntegerField()
    Under_Over_Budget=models.IntegerField()
    # user = models.ForeignKey(BaseModel, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)




def __str__(self):
    return self.username



