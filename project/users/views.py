from django.shortcuts import render, redirect
from django.contrib.auth.forms import authenticate
from .forms import RegistrationForm, MonthlyExpenseForm, AssetsForm, MiscFinancesForm, BaseForm as LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User
from . models import Assets, MonthlyExpenseModel
import math


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
    # Get a list of everything that a user as submit but filtering by date. 
    users_expenses=MonthlyExpenseModel.objects.all().filter(user=request.user).order_by('-created_date')
    users_assets=Assets.objects.all().filter(user=request.user).order_by('-created_date')

    if len(users_expenses)==0 or len(users_assets)==0:
        return redirect('budget')
    feedback=UserReview(users_expenses[0],users_assets[0])
    
    context={
        'users_expenses': users_expenses[0],
        'total_expenses': users_expenses[0].total_expenses,
        'users_assets': users_assets[0],
        'monthly_income': users_assets[0].monthly_income,
        'feedback': feedback,

    }
    
    return render(request, 'users/profile.html', context)

def base(request):
   
    return render(request, "users/base.html")



def budget(request):
    expenses=MonthlyExpenseForm()
    monthly_incomeform = AssetsForm()
    misc_finance_form = MiscFinancesForm()
    context={
        'monthlyExpense': expenses,
        'monthly_incomeform': monthly_incomeform,
        'misc_finance_form': misc_finance_form,
    }
   
    if request.method == "GET":
       form = monthly_incomeform

    else:
    #     # Create a form instance and populate it with data from the request:
        form = AssetsForm(request.POST)
        formTwo = MonthlyExpenseForm(request.POST)
        miscForm = MiscFinancesForm(request.POST)
    #     # Check if the form is valid:
        
        if form.is_valid() and formTwo.is_valid() and miscForm.is_valid():
     # Process the data in form.cleaned_data as required
            saveAssets(form, miscForm, request)
            saveMonthlyExpenses(formTwo, miscForm, request)

    
        return redirect('profile')
    return render(request,'users/budget.html', context)


#Future Page
def futureInvest(request):
    return render(request, 'users/futureinvest.html')


def saveAssets(form, miscForm, request):

    # Create a new assent object and save to the database
    new_asset=Assets()
    new_asset.monthly_income=form.cleaned_data['monthly_income']
    new_asset.amount_in_savings=form.cleaned_data['amount_in_savings']
    new_asset.interest_rate_on_savings_account=miscForm.cleaned_data['interest_rate_on_savings_account'] #done
    new_asset.amount_in_stocks=form.cleaned_data['amount_in_stocks']
    new_asset.investing_in_401K=miscForm.cleaned_data['investing_in_401K']#done
    new_asset.interest_401K_match=miscForm.cleaned_data['interest_401K_match']#done
    new_asset.monthly_amount_investing_in_roth=miscForm.cleaned_data['monthly_amount_investing_in_roth']
    # new_asset.roth_amount=form.cleaned_data['roth_amount']
    # new_asset.pass_miscellaneous=form.cleaned_data['pass_miscellaneous']
    new_asset.user=request.user
    total_Assets=new_asset.monthly_income + new_asset.amount_in_savings + new_asset.amount_in_stocks
    new_asset.total_Assets=total_Assets
    new_asset.save()

def saveMonthlyExpenses(formTwo, miscForm, request):
    new_expense=MonthlyExpenseModel()
    new_expense.car_payment=formTwo.cleaned_data['car_payment'] #done
    new_expense.rent_or_mortgage_payment=formTwo.cleaned_data['rent_or_mortgage_payment'] #done
    # new_expense.mortgage_bill=formTwo.cleaned_data['mortgage_bill']
    new_expense.mortgage_interest_rate=miscForm.cleaned_data['mortgage_interest_rate'] #done
    new_expense.groceries=formTwo.cleaned_data['groceries'] 
    new_expense.dining_out=formTwo.cleaned_data['dining_out']
    new_expense.gas=formTwo.cleaned_data['gas'] #done
    new_expense.utilites=formTwo.cleaned_data['utilites']
    new_expense.internet=formTwo.cleaned_data['internet'] #done
    new_expense.phone_bill=formTwo.cleaned_data['phone_bill']#done
    new_expense.miscellaneous=formTwo.cleaned_data['miscellaneous']
    new_expense.user=request.user
    total_expenses=new_expense.car_payment + new_expense.rent_or_mortgage_payment + new_expense.groceries + new_expense.dining_out + new_expense.gas + new_expense.internet + new_expense.utilites + new_expense.phone_bill + new_expense.miscellaneous
    new_expense.total_expenses=total_expenses
    new_expense.save()


def UserReview(user_expenses,user_assets):
    neg_advice_list=[]
    pro_advice_list=[]
    total=''
    print(total)
    Over_all_budget=user_assets.monthly_income -user_expenses.total_expenses
    if Over_all_budget<=0:
        total=(f'Monthly spending is {Over_all_budget} and is in the negative')
    else:
        total=(f'Monthly spending is {Over_all_budget} and is in the postive')


    if user_expenses.car_payment>=(user_assets.monthly_income*.1):
        neg_advice_list.append(f'Your car payment is higher than recommended. We recommend your car payment be no more then 10% percent of your monthly income. Try to reduce your car payment to ${math.floor(user_assets.monthly_income*.1)}')
    else: 
        pro_advice_list.append("Your car payment is less then 10% of your income and is within the recommended range.")

    if user_expenses.rent_or_mortgage_payment>=(user_assets.monthly_income*.3):
        neg_advice_list.append(f'Your rent or mortgage payment is high. We recommend your housing expenses be no more than 30% of your budget. Try to reduce your housing expense be ${math.floor(user_assets.monthly_income*.3)}')
    else: 
        pro_advice_list.append("Your rent or mortgage payment is less then 30% of your income and is within the recommended range.")

    if user_expenses.mortgage_interest_rate>5:
        neg_advice_list.append("Your mortgage interest rate is high. We recommend considering refinancing to lower your mortgage interest rate.")
    else:
        pro_advice_list.append('Your mortgage interest rate is at good level. The lower your interest rate, the more money you can save and invest.')

    if user_expenses.groceries>=(user_assets.monthly_income):
        neg_advice_list.append(f"Your grocery bill each month is at {user_expenses.groceries} and is high. We recommend that an individual should spend around $250 a month per person on groceries")
    else:
        pro_advice_list.append(f"Your grocery bill is at good amount at {user_expenses.groceries}. This is within 250 dollors per person each month")
    if user_expenses.gas>=200:
         neg_advice_list.append(f'Your monthly gas payment is {user_expenses.gas}. The average person in US spends $200 a month on gas. You should seek ways to decrease your cost of gas')
    else:
        pro_advice_list.append(f"The average person in US spends $200 a month on gas. You are within or below that amount, good job.")
    if user_expenses.internet>=90:
        neg_advice_list.append('The average cost of internet within the U.S is $60 to $90 per month. We recommend you look for cheaper internet provider to decrease your monthly expense.')
    else:
        pro_advice_list.append('You are within the average monthly cost for internet of $60 to $90 per month.')
    if user_expenses.phone_bill>=114:
        neg_advice_list.append('Phone bills can get costly. Your phone bill is above the average monthly spending of $114 per month. You can seek to decrease your phone bill by switching services or having friends or family join your plan to get additional discounts.')
    else:   
        pro_advice_list.append(f'Your phone bill of {user_expenses.phone_bill} is low and within good standing of being below $114 dollars per month')

    #Assets FeedBack
    if user_assets.interest_rate_on_savings_account<=.1:
        neg_advice_list.append(f"There are a lot of savings accounts that have high interest rates that can help generate some passive income. You indicated your bank account interest rate is {user_assets.interest_rate_on_savings_account}%. There are many savings acocunts that offer up to 5% interest rate.")
    else:
        pro_advice_list.append(f"Your bank interest rate is {user_assets.interest_rate_on_savings_account}%. You have a savings account with high interest rate. Because of this your money is not losing as much value and you have some passive income; good job.")
    if user_assets.investing_in_401K==0:
        neg_advice_list.append(f" You selected {user_assets.investing_in_401K} for investing into a 401K. Some companies offer 401Ks that you can invest in. You can invest into the 401K and Roth IRA at the same time. Considering asking your employer if they offer 401K benefits.")
    else:
        pro_advice_list.append(f'You selected {user_assets.investing_in_401K} for investing into a 401K. A 401K is good financial tool to help with retirement.')

    if user_assets.interest_401K_match<3:
        neg_advice_list.append(f'You indicated that your 401K match rate is {user_assets.interest_401K_match} percent. Most 401K offer more then 3% matching. This means if you input 3% of your pay check to 401K, your employer will also match up to 3 percent into your 401K. As result you will have 6% each month go into your 401K. You should seek to see if your employer as better 401K plans or possible seek for another job where the employer offeres a higher match rate.')
    else:
        pro_advice_list.append(f'You indicated that your 401K interest rate is {user_assets.interest_401K_match} percent. Your 401K match is within the normal range of 3 to 5 percent match rate. You should always seek to max your 401k match rate. For example, if your employer offers up to 5 percent match rate. You should invest at least 5 percent into 401K. Its free money that your employer is offering to give you for your retirment.')

    
    
    return {'negative': neg_advice_list, 'positive': pro_advice_list, 'total': total}


