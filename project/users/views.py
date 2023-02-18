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
        'total_Assets': users_assets[0].total_Assets,
        'feedback': feedback
        # 'expensesTotal': expensesTotal
    }
    
    return render(request, 'users/profile.html', context)

def base(request):
    # context= {
    #     form:'forms'
    # }
    return render(request, "users/base.html")


# def expencesTotal(request):
#     BlogPost.objects.filter(
#         user=request.user)

# def expences(request):
#     if ammount_cars>=(expencesTotal*.1):
#         print('Your car payment is to high. Your car payment should be 10% percent of you budget')
#         else: "You car payment is within budget"

#     if gas>=(expenceTotal*.1):
#         print('Your car payment is to high. Your car payment should be no more then 10% percent of you budget')

#     if rent>=(expencesTotal*.3)
#         print("Your rent is expense is high. Most advisers recommended 30% or lower of your monthly_income should go to housing")
    




def budget(request):
    expenses=MonthlyExpenseForm()
    monthly_incomeform = AssetsForm()
    # BudgetReview=BudgetReviewForm()
    context={
        'monthlyExpense': expenses,
        'monthly_incomeform': monthly_incomeform,
        # 'BudgetOut': BudgetReview

    }
    #   if request.method == "GET":
    #     form = RegistrationForm
    if request.method == "GET":
       form = monthly_incomeform

    else:
    #     # Create a form instance and populate it with data from the request:
        form = AssetsForm(request.POST)
        formTwo = MonthlyExpenseForm(request.POST)
    #     # Check if the form is valid:
        
        if form.is_valid() and formTwo.is_valid():
     # Process the data in form.cleaned_data as required
            saveAssets(form, request)
            saveMonthlyExpenses(formTwo, request)

    
        return redirect('profile')
    return render(request,'users/budget.html', context)


def saveAssets(form, request):

    # Create a new assent object and save to the database
    new_asset=Assets()
    new_asset.monthly_income=form.cleaned_data['monthly_income']
    new_asset.amount_in_savings=form.cleaned_data['amount_in_savings']
    new_asset.interest_rate_on_savings_account=form.cleaned_data['interest_rate_on_savings_account'] #done
    new_asset.amount_in_stocks=form.cleaned_data['amount_in_stocks']
    new_asset.investing_in_401K=form.cleaned_data['investing_in_401K']#done
    new_asset.interest_401K_match=form.cleaned_data['interest_401K_match']#done
    new_asset.monthly_amount_investing_in_roth=form.cleaned_data['monthly_amount_investing_in_roth']
    # new_asset.roth_amount=form.cleaned_data['roth_amount']
    # new_asset.pass_miscellaneous=form.cleaned_data['pass_miscellaneous']
    new_asset.user=request.user
    total_Assets=new_asset.monthly_income + new_asset.amount_in_savings + new_asset.amount_in_stocks
    new_asset.total_Assets=total_Assets
    new_asset.save()

def saveMonthlyExpenses(formTwo, request):
    new_expense=MonthlyExpenseModel()
    new_expense.car_payment=formTwo.cleaned_data['car_payment'] #done
    new_expense.rent_or_mortgage_payment=formTwo.cleaned_data['rent_or_mortgage_payment'] #done
    # new_expense.mortgage_bill=formTwo.cleaned_data['mortgage_bill']
    new_expense.mortgage_interest_rate=formTwo.cleaned_data['mortgage_interest_rate'] #done
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
    if user_expenses.car_payment>=(user_assets.monthly_income*.1):
        neg_advice_list.append('Your car payment is to high. Your car payment should be no more then 10% percent of you budget')
        # print('Your car payment is to high. Your car payment should be 10% percent of you budget')
    else: 
        pro_advice_list.append("You car payment is within budget, is less then 10% of your income")

    if user_expenses.rent_or_mortgage_payment>=(user_assets.monthly_income*.3):
        neg_advice_list.append('Your rent or mortgage payment is to high. Your housing expense should less 30% of your budget')
    else: 
        pro_advice_list.append("You rent or mortgage payment is within budget, and is less then 30% of your income")
#         print("Your rent is expense is high. Most advisers recommended 30% or lower of your monthly_income should go to housing")
    if user_expenses.mortgage_interest_rate>5:
        neg_advice_list.append("Your mortgage interest rate is high. Possible seek to refinance to lower your mortgage interest rate.")
    else:
        pro_advice_list.append('Your mortgage is at good level. The lower your interest rate, the more money you can save in mortgage low.')

    if user_expenses.groceries>=(user_assets.monthly_income):
        neg_advice_list.append("You grocerie cost per month is to high. The average cost per person to cost that individual should spend on groceries is $250 a month.")
    else:
        pro_advice_list.append('Your grocerie budget is at good amount, and is within 250 dollors per person each month')
    if user_expenses.gas>=200:
         neg_advice_list.append('Average person in US. Spends $200 a month on gas. You should seek ways to decrease your cost of gas spending.')
    else:
        pro_advice_list.append("Average person in US. Spends $200 a month on gas. You are within or below that cost averge, good job.")
    if user_expenses.internet>=90:
        neg_advice_list.append('The average Interent cost within the U.S is 60 to 90 dollors per month. You could seek to decrease your cost of internet by looking for cheaper companies.')
    else:
        pro_advice_list.append('You are within the average speanding on internet.')
    if user_expenses.phone_bill>=114:
        neg_advice_list.append('Phone bills can get costly. Your phone bill is above the average monthly spending of $114 per month. You can seek to decrease your phone bill by swithing services or having friends or family join your plan to make it lower.')
    else:   
        pro_advice_list.append('Phone Bill you have is low and within good standing of being below $114 dollars per month')

    #Assents FeedBack
    if user_assets.interest_rate_on_savings_account<=.1:
        neg_advice_list.append("There alot of savings accounts that have high interest rates that can help make some passive income. Currently you have bank account that dosen't have a good interest rate. You can find bank acocunts up to 5% interest rate. You can find a better oppurnity by placing your money into high intest rate savings account")
    else:
        pro_advice_list.append('You have bank savings account with high interest rate, because of this your money is not lossing as much value and you have some passive income, good job.')
    if user_assets.investing_in_401K==0:
        neg_advice_list.append("Some companies have 401K that you can invest in. You can invest and roth at the sametime. You could seek your employer to see if they offer 401K.")
    else:
        pro_advice_list.append('Your investing 401K, and is good fincial tool to help with retirment.')
    if user_assets.interest_401K_match<3:
        neg_advice_list.append('Most 401K offer more then 3% matching. This means if you input 3% of your pay check to 401K, your employer will also match up to 3 percent into your 401K. As result you will have 6% each month go into your 401K. You should seek to see if your employer as better 401K plans or possible seek for another job where the other employer as a higher 401K match rate.')
    else:
        pro_advice_list.append('Your 401K match is within the normal range of 3 to 5 percent match rate. You should always seek to max your 401k match rate. For example, if your employer offers up to 5 percent match rate. You should invest at least 5 percent into 401K. Its free money that your employer is offering to give you for your retirment.')

    
    
    return {'negative': neg_advice_list, 'positive': pro_advice_list}
    # return [neg_advice_list, pro_advice_list]

    



# def expencesTotal(request):
#     BlogPost.objects.filter(
#         user=request.user)

# def expences(request):
#     if ammount_cars>=(expencesTotal*.1):
#         print('Your car payment is to high. Your car payment should be 10% percent of you budget')
#         else: "You car payment is within budget"

#     if gas>=(expenceTotal*.1):
#         print('Your car payment is to high. Your car payment should be no more then 10% percent of you budget')

#     if rent>=(expencesTotal*.3)
#         print("Your rent is expense is high. Most advisers recommended 30% or lower of your monthly_income should go to housing")


  
    # print(f'great stuff{users_expenses}')
    # for expenses in users_expenses:
    #     print(expenses.car_payment )
    # print(users_expenses[1].car_payment )



    # def index(request):
    # # Get all public posts and order by date created (newest first)
    # posts = BlogPost.objects.all().order_by('-created_date')
    # return render(request, 'blog/index.html', {"posts": posts})
