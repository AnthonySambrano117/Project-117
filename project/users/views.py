from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationModelForm
# from django.contrib.auth.views import LoginView
# Create your views here.


def registerPage(request):
    form=UserCreationForm()
    context={'form':form}
    # If its a get regisiter it will just take the user back to the regisiter page
    if request.method == "GET":
        form = UserCreationForm()

    # else:
    #     # Create a form instance and populate it with data from the request:
    #     form = RegistrationForm(request.POST)
    #     # Check if the form is valid:
    #     if form.is_valid():
    #         # Process the data in form.cleaned_data as required
    #         username = form.cleaned_data['username']
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']  # password123
    #         password_confirmation = form.cleaned_data['password_confirmation']

    #     if password == password_confirmation:
    #         # Create a new user
    #         user = User()
    #         user.username = username
    #         user.email = email
    #         # Do not store the plain text password on the user model.
    #         # user.password = password
    #         # use .set_password() instead to store the hashed password to the db
    #         user.set_password(password)
    #         user.save()
    #         return redirect('profile')

    # return render(request, 'users/register.html', {'form': form})

    return render(request, 'users/register.html',context)

        

    # If this is a POST request then process the Form data
    

            # Check if the passwords match
         