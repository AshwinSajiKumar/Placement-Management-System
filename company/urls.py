from django.urls import path
from company import views

urlpatterns = [
    path('login/', views.company_login, name='company_login'),
    path('logout/', views.company_logout, name='company_logout'),
    path('home/', views.company_home, name='company_home'),
    path('post-job/', views.post_job, name='post_job'),
    path('view-applications/<int:job_id>/', views.view_applications, name='view_applications'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
     path('student-details/<int:student_id>/', views.student_details, name='student_details'),
    path('update-application-status/<int:application_id>/<str:status>/', views.update_application_status, name='update_application_status'),
    # Add more URLs for other views
]
