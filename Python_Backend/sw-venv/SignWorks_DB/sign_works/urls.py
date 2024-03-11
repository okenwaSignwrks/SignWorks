from django.urls import path
from . import views

urlpatterns = [
    path('customer_list/', views.customer_list, name="customerlist"),
    path('entry_list/', views.entrylist, name='entrylist'),
    path('plan_status/', views.plan_status, name='planstatus'),
    path('job_id/', views.get_jobs, name='jobids'),
    path('plan_status_view/', views.plan_status_view, name="planstatusview"),
    path('customer_detail/<int:job_no>/<str:customer>/', views.customer_detail, name='customerdetail'),
    path('customer_update/<int:job_no>/', views.customer_update, name='customerupdate'),
    path('plan_status_update/<int:job_no>/', views.plan_status_update, name='planstatusupdate'),
    path('permits/', views.permits, name='permits'),
    path('permits/<int:job_no>/', views.permits, name='permit-update')

]
