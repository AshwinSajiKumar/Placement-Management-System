from django.urls import path
from . import views

app_name = 'student_import'
urlpatterns = [
    path('login/', views.login_view, name='csvlogin'),
    path('student-list/', views.student_list_view, name='student_list'),
    path('csv-import/', views.csv_import_view, name='csv_import'), 
    path('logout/', views.logout_view, name='csvlogout'),
]
