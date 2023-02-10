# Generated by Django 4.1.5 on 2023-02-10 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegistrationForm',
            new_name='RegistrationModel',
        ),
        migrations.CreateModel(
            name='MonthlyExpenseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_cars', models.IntegerField()),
                ('rent_bill', models.IntegerField()),
                ('mortgage_bill', models.IntegerField()),
                ('mortgage_interest_rate', models.IntegerField()),
                ('gorcerys', models.IntegerField()),
                ('dinning_out', models.IntegerField()),
                ('gas', models.IntegerField()),
                ('internet', models.IntegerField()),
                ('phone_bill', models.IntegerField()),
                ('utilites', models.IntegerField()),
                ('miscellaneous', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.basemodel')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_Monthly_Savings', models.IntegerField()),
                ('Total_Monthly_Expenses', models.IntegerField()),
                ('Under_Over_Budget', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.basemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.IntegerField()),
                ('savings_amount', models.IntegerField()),
                ('savings_interest_rate', models.IntegerField()),
                ('amount_in_stocks', models.IntegerField()),
                ('yes_no_401K', models.CharField(max_length=3)),
                ('interest_401K_match', models.IntegerField()),
                ('roth_investing', models.IntegerField()),
                ('roth_amount', models.IntegerField()),
                ('pass_miscellaneous', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.basemodel')),
            ],
        ),
    ]