from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Company, Job,JobApplication
from .forms import JobForm
from django.contrib import messages
from register.models import Student
from std_app.models import StudentDetails


def company_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('company_home')
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'company_login.html', {'error_message': error_message})
    else:
        return render(request, 'company_login.html')

def company_logout(request):
    logout(request)
    return redirect('company_login')

@login_required(login_url='company_login')
def company_home(request):
    company = Company.objects.get(user=request.user)
    jobs = Job.objects.filter(company=company)
    job_applications = JobApplication.objects.filter(job__in=jobs)
    students = Student.objects.filter(jobapplication__in=job_applications).distinct()
    context = {
        'company': company,
        'jobs': jobs,
        'students': students,
    }
    return render(request, 'company_home.html', context)

@login_required(login_url='company_login')
def post_job(request):
    company = Company.objects.get(user=request.user)
    job = Job.objects.filter(company=company).first()

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()
            messages.success(request, 'Job posted successfully.')
            return redirect('company_home')
    else:
        form = JobForm(instance=job)

    context = {
        'company': company,
        'form': form,
    }
    return render(request, 'post_job.html', context)



@login_required(login_url='company_login')
def view_applications(request, job_id):
    job = Job.objects.get(id=job_id)
    applications = JobApplication.objects.filter(job=job).select_related('student__user')
    context = {
        'job': job,
        'applications': applications,
    }
    return render(request, 'view_applications.html', context)


@login_required(login_url='company_login')
def update_application_status(request, application_id, status):
    application = get_object_or_404(JobApplication, id=application_id)
    job = application.job

    # Check if the job belongs to the current company
    if job.company.user == request.user:
        application.status = status
        application.save()
        messages.success(request, 'Application status changed successfully.')
    else:
        messages.error(request, 'You are not authorized to change this application status.')

    return redirect('view_applications', job_id=job.id)


@login_required(login_url='company_login')
def delete_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if job.company.user == request.user:
        job.delete()
        messages.success(request, 'Job deleted successfully.')
    else:
        messages.error(request, 'You are not authorized to delete this job.')
    return redirect('company_home')


@login_required
def student_details(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student_details = get_object_or_404(StudentDetails, user=student.user)

    context = {
        'student': student,
        'student_details': student_details,
    }

    return render(request, 'student_details.html', context)


