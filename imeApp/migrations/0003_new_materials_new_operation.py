# Generated by Django 4.0.1 on 2022-03-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imeApp', '0002_computer_cost_distribution_employee_engineering_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200)),
                ('meaning', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='new_Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200)),
                ('meaning', models.TextField()),
            ],
        ),
    ]
