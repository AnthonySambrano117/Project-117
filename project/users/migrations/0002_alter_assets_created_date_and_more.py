# Generated by Django 4.1.5 on 2023-02-15 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='created_date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='monthlyexpensemodel',
            name='created_date',
            field=models.DateTimeField(default=''),
        ),
    ]
