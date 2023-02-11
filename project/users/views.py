from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, authenticate
from .forms import RegistrationForm, MonthlyExpenseForm, AssetsForm, BudgetReviewForm, BaseForm as LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User
from . models import Assets, MonthlyExpenseModel, BudgetReview
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
    expenses=MonthlyExpenseForm()
    incomeform = AssetsForm()
    # BudgetReview=BudgetReviewForm()
    context={
        'monthlyExpense': expenses,
        'incomeform': incomeform,
        # 'BudgetOut': BudgetReview

    }
    #   if request.method == "GET":
    #     form = RegistrationForm
    if request.method == "GET":
       form = incomeform

    else:
    #     # Create a form instance and populate it with data from the request:
        form = AssetsForm(request.POST)
        formTwo = MonthlyExpenseForm(request.POST)
    #     # Check if the form is valid:
        
        if form.is_valid():
     # Process the data in form.cleaned_data as required
            saveAssets(form, request)
            saveMonthlyExpenses(formTwo, request)

            # income=form.cleaned_data['income']
            # savings_amount=form.cleaned_data['savings_amount']
            # savings_interest_rate=form.cleaned_data['savings_interest_rate']
            # amount_in_stocks=form.cleaned_data['amount_in_stocks']
            # yes_no_401K=form.cleaned_data['yes_no_401K']
            # interest_401K_match=form.cleaned_data['interest_401K_match']
            # roth_investing=form.cleaned_data['roth_investing']
            # roth_amount=form.cleaned_data['roth_amount']
            # pass_miscellaneous=form.cleaned_data['pass_miscellaneous']

            # # Create a new assent object and save to the database
            # new_assent=Assets()
            # new_assent.income=income
            # new_assent.savings_amount=savings_amount
            # new_assent.savings_interest_rate=savings_interest_rate
            # new_assent.amount_in_stocks=amount_in_stocks
            # new_assent.yes_no_401K=yes_no_401K
            # new_assent.interest_401K_match=interest_401K_match
            # new_assent.roth_investing=roth_investing
            # new_assent.roth_amount=roth_amount
            # new_assent.pass_miscellaneous=pass_miscellaneous
            # new_assent.user=request.user
            # new_assent.save()
            # print(request.user)
            # print(context)
            # print(new_assent)

    return render(request,'users/budget.html', context)


def saveAssets(form, request):

    # Create a new assent object and save to the database
    new_assent=Assets()
    new_assent.income=form.cleaned_data['income']
    new_assent.savings_amount=form.cleaned_data['savings_amount']
    new_assent.savings_interest_rate=form.cleaned_data['savings_interest_rate']
    new_assent.amount_in_stocks=form.cleaned_data['amount_in_stocks']
    new_assent.yes_no_401K=form.cleaned_data['yes_no_401K']
    new_assent.interest_401K_match=form.cleaned_data['interest_401K_match']
    new_assent.roth_investing=form.cleaned_data['roth_investing']
    new_assent.roth_amount=form.cleaned_data['roth_amount']
    new_assent.pass_miscellaneous=form.cleaned_data['pass_miscellaneous']
    new_assent.user=request.user
    new_assent.save()

def saveMonthlyExpenses(formTwo, request):
    new_expense=MonthlyExpenseModel()
    new_expense.amount_cars=formTwo.cleaned_data['amount_cars']
    new_expense.rent_bill=formTwo.cleaned_data['rent_bill']
    new_expense.mortgage_bill=formTwo.cleaned_data['mortgage_bill']
    new_expense.mortgage_interest_rate=formTwo.cleaned_data['mortgage_interest_rate']
    new_expense.gorcerys=formTwo.cleaned_data['gorcerys']
    new_expense.dinning_out=formTwo.cleaned_data['dinning_out']
    new_expense.gas=formTwo.cleaned_data['gas']
    new_expense.utilites=formTwo.cleaned_data['utilites']
    new_expense.internet=formTwo.cleaned_data['internet']
    new_expense.phone_bill=formTwo.cleaned_data['phone_bill']
    new_expense.miscellaneous=formTwo.cleaned_data['miscellaneous']
    new_expense.user=request.user
    new_expense.save()

# def saveAssets(form, request):
#     income=form.cleaned_data['income']
#     savings_amount=form.cleaned_data['savings_amount']
#     savings_interest_rate=form.cleaned_data['savings_interest_rate']
#     amount_in_stocks=form.cleaned_data['amount_in_stocks']
#     yes_no_401K=form.cleaned_data['yes_no_401K']
#     interest_401K_match=form.cleaned_data['interest_401K_match']
#     roth_investing=form.cleaned_data['roth_investing']
#     roth_amount=form.cleaned_data['roth_amount']
#     pass_miscellaneous=form.cleaned_data['pass_miscellaneous']

#     # Create a new assent object and save to the database
#     new_assent=Assets()
#     new_assent.income=income
#     new_assent.savings_amount=savings_amount
#     new_assent.savings_interest_rate=savings_interest_rate
#     new_assent.amount_in_stocks=amount_in_stocks
#     new_assent.yes_no_401K=yes_no_401K
#     new_assent.interest_401K_match=interest_401K_match
#     new_assent.roth_investing=roth_investing
#     new_assent.roth_amount=roth_amount
#     new_assent.pass_miscellaneous=pass_miscellaneous
#     new_assent.user=request.user
#     new_assent.save()

# def FinacneReview():

    