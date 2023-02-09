from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, authenticate
from .forms import RegistrationForm, MonthlyExpenseForm, AssentsForm, BudgetReviewForm, BaseForm as LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User
# from django.contrib.auth.views import LoginView
# Create your views here.

# from django.shortcuts import render, redirect



# from blog.models import BlogPost


# Login view - login a user
def login(request):
    # If this is a GET request then create the default form
    if request.method == "GET":
        form = LoginForm()
    # If this is a POST request then process the Form data
    else:
        # Create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            username_input = form.cleaned_data['username']
            password_input = form.cleaned_data['password']
            # Authenticate the user
            user = authenticate(
                request, username=username_input, password=password_input)
            # If user is found then log them in
            if user is not None:
                user_login(request, user)
                # If the user was trying to access a page before logging in
                # then redirect them to that page
                return redirect('profile')
                previous_page = request.GET.get('next')
                # If previous_page is not None then redirect to that page
                if previous_page is not None:
                    return redirect(previous_page)
                # If previous_page is None then redirect to the profile page
                else:
                    return redirect('profile')

    return render(request, "users/login.html", {"form": form})


def logout(request):
    user_logout(request)
    return redirect('login')

def registerPage(request):
    form=RegistrationForm
    context={'form':form}
    # If its a get regisiter it will just take the user back to the regisiter page
    if request.method == "GET":
        form = RegistrationForm
    else:
        # Create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']  # password123
            password_confirmation = form.cleaned_data['password_confirmation']

        if password == password_confirmation:
            # Create a new user
            user = User()
            user.username = username
            user.email = email
            # Do not store the plain text password on the user model.
            # user.password = password
            # use .set_password() instead to store the hashed password to the db
            user.set_password(password)
            user.save()
            return redirect('login')

    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    # Get all blogposts by user from db
    # posts = BlogPost.objects.filter(
    #     user=request.user).order_by('-created_date')
    # Put all posts into context
    # context = {
    #     # "posts": posts
    #     'forms':form
    # }
    # Pass context into template
    print(request)
    return render(request, 'users/profile.html')

def base(request):
    # context= {
    #     form:'forms'
    # }
    return render(request, "users/base.html")


def expencesTotal(request):
    BlogPost.objects.filter(
        user=request.user)

# def expences(request):
#     if ammount_cars>=(expencesTotal*.1):
#         print('Your car payment is to high. Your car payment should be 10% percent of you budget')
#         else: "You car payment is within budget"

#     if gas>=(expenceTotal*.1):
#         print('Your car payment is to high. Your car payment should be no more then 10% percent of you budget')

#     if rent>=(expencesTotal*.3)
#         print("Your rent is expense is high. Most advisers recommended 30% or lower of your income should go to housing")
    
# amount_cars=models.IntegerField()
#     rent_bill=models.IntegerField()
#     mortgage_bill=models.IntegerField()
#     mortgage_interest_rate=models.IntegerField()
#     gorcerys=models.IntegerField()
#     dinning_out=models.IntegerField()
#     gas=models.IntegerField()
#     internet=models.IntegerField()
#     phone_bill=models.IntegerField()
#     utilites=models.IntegerField()
#     miscellaneous=models.IntegerField()
#     user = models.ForeignKey(BaseModel, on_delete=models.CASCADE)




def budget(request):
    form=MonthlyExpenseForm()
    incomeform = AssentsForm()
    BudgetReview=BudgetReviewForm()
    context={
        # 'forms':form,
        'incomeform': incomeform,
        # 'BudgetOut': BudgetReview

    }
    print(context)
    #   if request.method == "GET":
    #     form = RegistrationForm
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
    return render(request,'users/budget.html', context)
    