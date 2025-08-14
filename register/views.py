from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProfileImageForm
from company.models import JobApplication,Company
from .models import Student, Stats
from django.contrib.auth.models import  auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
import os
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import never_cache



def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student_list.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and not user.is_superuser:
            auth.login(request, user)
            student = Student.objects.get(user=user)
            # Store the student ID in the session
            request.session['student_id'] = student.id
            return redirect('student-home')
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'student_login.html', {'error_message': error_message})

    return render(request, 'student_login.html')

@never_cache
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
@never_cache
def student_home(request):
    try:
        student = Student.objects.get(user=request.user)
        stats = Stats.objects.all()
        total_students = Student.objects.count()
        placed_students = JobApplication.objects.filter(status='PLACED').count()
        company_users = Company.objects.count()

        context = {
            'student': student,
            'stats': stats,
            'total_students':total_students,
            'placed_students': placed_students,
            'company_users': company_users,
        }
    except (Student.DoesNotExist, ObjectDoesNotExist):
        # Handle case where student object does not exist
        return redirect('login')
    
    # Handle missing student image gracefully
    if not student.image:
        # Use a default image path that exists in static files
        student.image = '/static/images/default_image.jpg'
    
    return render(request, 'student_home.html', context)

@login_required(login_url='login')
@never_cache
def update_profile_image(request):
    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.student)
        if form.is_valid():
            form.save()
            return redirect('student-home')  # Redirect to the student's profile page
    else:
        form = ProfileImageForm(instance=request.user.student)
    return render(request, 'update_profile_image.html', {'form': form})


