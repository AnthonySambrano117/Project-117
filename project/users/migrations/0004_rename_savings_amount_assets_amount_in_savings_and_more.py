# Generated by Django 4.1.5 on 2023-02-15 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_assets_total_assets_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets',
            old_name='savings_amount',
            new_name='Amount_In_Savings',
        ),
        migrations.RenameField(
            model_name='monthlyexpensemodel',
            old_name='total_Expenses',
            new_name='total_expenses',
        ),
    ]
