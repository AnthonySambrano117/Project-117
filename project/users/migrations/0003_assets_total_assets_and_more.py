# Generated by Django 4.1.5 on 2023-02-15 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_assets_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='total_Assets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthlyexpensemodel',
            name='total_Expenses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='assets',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='monthlyexpensemodel',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
