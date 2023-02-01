from django.forms import ModelForm
from .models import RegistrationForm



class RegistrationModelForm(ModelForm):
    class Profile:
        model=RegistrationForm
        fields=['username', 'password', 'email']

# class BaseForm(forms.Form):
#     username = forms.CharField(max_length=32, min_length=3)
#     password = forms.CharField(
#         widget=forms.PasswordInput(), min_length=8, max_length=32)


# # Create a form class that inherits from BaseForm
# class RegistrationForm(BaseForm):
#     email = forms.EmailField()
#     password_confirmation = forms.CharField(min_length=8, max_length=32)