# Generated by Django 3.2 on 2024-02-16 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('job_no', models.IntegerField()),
                ('customer', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('job_description', models.CharField(max_length=200)),
                ('price_amount', models.CharField(blank=True, max_length=15, null=True)),
                ('permit_status', models.CharField(blank=True, max_length=20, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('invoice_no', models.IntegerField()),
                ('payment_method', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permits',
            fields=[
                ('job_no', models.IntegerField(primary_key=True, serialize=False)),
                ('client', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('date_submitted', models.DateField()),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Not Submitted', 'Not Submitted')], max_length=20)),
                ('date_approved', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
