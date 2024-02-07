from django.db import models
from djongo import models

class CustomerList(models.Model):
    date = models.DateField()
    job_no = models.IntegerField(max_length=4)
    customer = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    job_description = models.CharField(max_length=200)
    price_amount = models.CharField(max_length=15)
    permit_status = models.CharField(max_length=20, blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    invoice_no = models.IntegerField(max_length=6)
    payment_method = models.CharField(max_length=30)

class Status(models.TextChoices):
    approved = 'Approved'
    pending = 'Pending'
    not_submitted = 'Not Submitted'

class Permits(models.Model):
    job_no = models.ForeignKey(CustomerList, on_delete=models.CASCADE)
    #client = models.ForeignKey(CustomerList, on_delete=models.CASCADE)
    date_submitted = models.DateField()
    status = models.CharField(max_length=20, choices=Status.choices)
    date_approved = models.DateField(blank=True, null=True)




