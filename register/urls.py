from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('student-home/', views.student_home, name='student-home'),
    path('student-list/', views.student_list, name='student-list'),
    path('update-profile-image/', views.update_profile_image, name='update_profile_image'),
]
