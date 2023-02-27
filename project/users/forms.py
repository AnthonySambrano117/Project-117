from django.forms import ModelForm
from .models import RegistrationModel
from django import forms



class BaseForm(forms.Form):
    username = forms.CharField(max_length=32, min_length=3, 
                    widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Password'}), min_length=8, max_length=32)

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
    rent_or_mortgage_payment=forms.IntegerField()
    car_payment =forms.IntegerField()
    # mortgage_bill=forms.IntegerField()
    # mortgage_interest_rate=forms.IntegerField()
    groceries=forms.IntegerField()
    dining_out=forms.IntegerField()
    gas=forms.IntegerField()
    internet=forms.IntegerField()
    phone_bill=forms.IntegerField()
    utilites=forms.IntegerField()
    miscellaneous=forms.IntegerField()

class AssetsForm(forms.Form):
    # select_choices=(
    #     ('Yes', 'Yes'),
    #     ('No', 'No'),
    # )

    monthly_income=forms.IntegerField()
    amount_in_savings=forms.IntegerField()
    # interest_rate_on_savings_account=forms.IntegerField()
    amount_in_stocks=forms.IntegerField()
    # investing_in_401K=forms.ChoiceField(choices=select_choices)
    # interest_401K_match=forms.IntegerField()
    # monthly_amount_investing_in_roth=forms.IntegerField()
    # roth_amount=forms.IntegerField()
    # pass_miscellaneous=forms.IntegerField()
    # user = forms.ForeignKey(BaseModel, on_delete=models.CASCADE)

class MiscFinancesForm(forms.Form):
    select_choices=(
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    mortgage_interest_rate=forms.IntegerField()
    interest_rate_on_savings_account=forms.IntegerField()
    investing_in_401K=forms.ChoiceField(choices=select_choices)
    interest_401K_match=forms.IntegerField()
    monthly_amount_investing_in_roth=forms.IntegerField()


class BudgetReviewForm(forms.Form):
    Total_Monthly_Savings=forms.IntegerField()
    Total_Monthly_Expenses=forms.IntegerField()
    Under_Over_Budget=forms.IntegerField()
    # user = models.ForeignKey(BaseModel, on_delete=models.CASCADE)

# class FinancialInfo(MonthlyExpenseForm, AssetsForm):






