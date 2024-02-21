from django.urls import path
from . import views

urlpatterns = [
    path('customer_list/', views.customer_list, name="customerlist"),
    path('entry_list/', views.entrylist, name='entrylist'),
    path('permit_status/', views.permit_status, name='permitstatus'),
    path('job_id/', views.get_jobs, name='jobids'),
    path('status_view/', views.status_view, name="statusview"),
    path('customer_detail/<int:job_no>/<str:customer>/', views.customer_detail, name='customerdetail'),
    path('customer_update/<int:job_no>/', views.customer_update, name='customerupdate'),
    path('status_update/<int:job_no>/', views.status_update, name='statusupdate')

]
