from django.db import models
from djongo import models

class CustomerList(models.Model):
    date = models.DateField()
    job_no = models.IntegerField()
    customer = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    job_description = models.CharField(max_length=200)
    price_amount = models.CharField(max_length=15, blank=True, null=True)
    permit_status = models.CharField(max_length=20, blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    invoice_no = models.IntegerField()
    payment_method = models.CharField(max_length=30, blank=True, null=True)

class Status(models.TextChoices):
    approved = 'Approved'
    pending = 'Pending'
    not_submitted = 'Not Submitted'

class Permits(models.Model):
    job_no = models.IntegerField(primary_key=True)
    client = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    date_submitted = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices)
    date_approved = models.DateField(null=True, blank=True)




