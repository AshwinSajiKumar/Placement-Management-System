from django.urls import path
from . import views

urlpatterns = [
        path('change-password/',views.change_password,name='change_password'),
        path('form/', views.form_details, name='form_details'),
        path('view-jobs/',views.view_jobs,name='view_jobs'),
        path('apply-job/<int:job_id>/', views.try_job, name='try_job'),
        path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
        path('remove-job/<int:job_id>/', views.erase_job, name='erase_job'),
        path('company/<int:company_id>/', views.company_details, name='company_details'),
]
