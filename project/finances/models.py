# from django.db import models

# # Create your models here.
# class BaseForm(forms.Form):
#     username = forms.CharField(max_length=32, min_length=3)
#     password = forms.CharField(
#         widget=forms.PasswordInput(), min_length=8, max_length=32)


# # Create a form class that inherits from BaseForm
# class RegistrationForm(BaseForm):
#     email = forms.EmailField()
#     password_confirmation = forms.CharField(min_length=8, max_length=32)

# """
# Todo
# title - Walk the dog
# description - Walk the dog for at least 2 miles
# completed - False
# """


# class Todo(models.Model):
#     title = models.CharField(max_length=75)
#     description = models.CharField(max_length=250)
#     completed = models.BooleanField(default=False)
#     created_date = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         # (False) Walk the dog - Walk the dog for at least 2 miles
#         return f"({self.completed}) {self.title} - {self.description}"