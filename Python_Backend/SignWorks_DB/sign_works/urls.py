from django.urls import path
from . import views

urlpatterns = [
    path('customer_list/', views.customer_list, name="customerlist"),
    path('entry_list/', views.entrylist, name='entrylist'),
    path('permit_status/', views.status, name='permitstatus')
]
