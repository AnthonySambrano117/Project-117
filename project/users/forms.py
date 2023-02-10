from django.forms import ModelForm
from .models import RegistrationModel
from django import forms



class BaseForm(forms.Form):
    username = forms.CharField(max_length=32, min_length=3)
    password = forms.CharField(
        widget=forms.PasswordInput(), min_length=8, max_length=32)

# # Create a form class that inherits from BaseForm
class RegistrationForm(BaseForm):
    email = forms.EmailField()
    password_confirmation = forms.CharField(min_length=8, max_length=32)

# class RegistrationModelForm(BaseForm):
#     class Meta:
#         model=RegistrationModel
#         fields=['username', 'password', 'email']
#         # exlude=['username']
class MonthlyExpenseForm(forms.Form):
    amount_cars=forms.IntegerField()
    rent_bill=forms.IntegerField()
    mortgage_bill=forms.IntegerField()
    mortgage_interest_rate=forms.IntegerField()
    gorcerys=forms.IntegerField()
    dinning_out=forms.IntegerField()
    gas=forms.IntegerField()
    internet=forms.IntegerField()
    phone_bill=forms.IntegerField()
    utilites=forms.IntegerField()
    miscellaneous=forms.IntegerField()

class AssetsForm(forms.Form):
    income=forms.IntegerField()
    savings_amount=forms.IntegerField()
    savings_interest_rate=forms.IntegerField()
    amount_in_stocks=forms.IntegerField()
    yes_no_401K=forms.CharField(max_length=3)
    interest_401K_match=forms.IntegerField()
    roth_investing=forms.IntegerField()
    roth_amount=forms.IntegerField()
    pass_miscellaneous=forms.IntegerField()
    # user = forms.ForeignKey(BaseModel, on_delete=models.CASCADE)

class BudgetReviewForm(forms.Form):
    Total_Monthly_Savings=forms.IntegerField()
    Total_Monthly_Expenses=forms.IntegerField()
    Under_Over_Budget=forms.IntegerField()
    # user = models.ForeignKey(BaseModel, on_delete=models.CASCADE)





