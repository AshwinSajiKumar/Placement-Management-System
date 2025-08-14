from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from register.models import Student
from .models import StudentDetails,ButtonState
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from company.models import Job,JobApplication,Company
import os
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from django.views.decorators.cache import never_cache
# Create your views here.



@login_required(login_url='login')
@never_cache
def change_password(request):
    if request.method=='POST':
        form =PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Your password has been changed successfully.")
            return redirect('/home/student-home/')
        else:
            messages.error(request,"Please correct the error below.")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'change_password.html',{'form':form})



@login_required(login_url='login')
@never_cache
def form_details(request):
    try:
        student = Student.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Handle case where student object does not exist
        return redirect('login')

    student_details = None


    if request.method == 'POST':
        uid = request.POST.get('uid')
        phno = request.POST.get('phone')
        PEmailId = request.POST.get('mailid')
        address = request.POST.get('address')
        Dob = request.POST.get('dob')
        Aadhar = request.POST.get('aadhaar')
        Pan = request.POST.get('pan')
        Passport = request.POST.get('passport')
        BloodGrp = request.POST.get('blood')
        Religion = request.POST.get('religion')
        Fathers_Name = request.POST.get('fname')
        Mothers_Name = request.POST.get('mname')
        Father_Occupation = request.POST.get('foccupation')
        Mother_Occupation = request.POST.get('moccupation')
        LocalGuardian_Ph = request.POST.get('lgphno')
        District = request.POST.get('district')
        Pincode = request.POST.get('pincode')
        TenthSchoolName = request.POST.get('tenthschool')
        TenthPercentage = request.POST.get('tenthpercentage')
        TenthPassoutYear = request.POST.get('tenthyear')
        TwelthSchoolName = request.POST.get('twelthschool')
        TwelthPercentage = request.POST.get('twelthpercentage')
        TwelthPassoutYear = request.POST.get('twelthyear')
        Keam = request.POST.get('keam')
        S_one = request.POST.get('one')
        S_two = request.POST.get('two')
        S_three = request.POST.get('three')
        S_four = request.POST.get('four')
        S_five = request.POST.get('five')
        S_six = request.POST.get('six')
        S_seven = request.POST.get('seven')
        S_eight = request.POST.get('eight')
        Current_CGPA = request.POST.get('cgpa')
        Supply_Count = request.POST.get('supply')
        LinkedIn = request.POST.get('linkedin')
        Internship = request.POST.get('internship')

        # Retrieve the current user's student details if they exist
        student_details = StudentDetails.objects.filter(user=request.user).first()

        if student_details:
            # Update the existing student details
            student_details.uid = uid
            student_details.phno = phno
            student_details.PEmailId = PEmailId
            student_details.address = address
            student_details.Dob = Dob
            student_details.Aadhar = Aadhar
            student_details.Pan = Pan
            student_details.Passport = Passport
            student_details.BloodGrp = BloodGrp
            student_details.Religion = Religion
            student_details.Fathers_Name = Fathers_Name
            student_details.Mothers_Name = Mothers_Name
            student_details.Father_Occupation = Father_Occupation
            student_details.Mother_Occupation = Mother_Occupation
            student_details.LocalGuardian_Ph = LocalGuardian_Ph
            student_details.District = District
            student_details.Pincode = Pincode
            student_details.TenthSchoolName = TenthSchoolName
            student_details.TenthPercentage = TenthPercentage
            student_details.TenthPassoutYear = TenthPassoutYear
            student_details.TwelthSchoolName = TwelthSchoolName
            student_details.TwelthPercentage = TwelthPercentage
            student_details.TwelthPassoutYear = TwelthPassoutYear
            student_details.Keam = Keam
            student_details.S_one = S_one
            student_details.S_two = S_two
            student_details.S_three = S_three
            student_details.S_four = S_four
            student_details.S_five = S_five
            student_details.S_six = S_six
            student_details.S_seven = S_seven
            student_details.S_eight = S_eight
            student_details.Current_CGPA = Current_CGPA
            student_details.Supply_Count = Supply_Count
            student_details.LinkedIn = LinkedIn
            student_details.Internship = Internship

            student_details.save()
        else:
            # Create a new student details entry
            student_details = StudentDetails(
                user=request.user,
                uid=uid,
                phno=phno,
                PEmailId=PEmailId,
                address=address,
                Dob=Dob,
                Aadhar=Aadhar,
                Pan=Pan,
                Passport=Passport,
                BloodGrp=BloodGrp,
                Religion=Religion,
                Fathers_Name=Fathers_Name,
                Mothers_Name=Mothers_Name,
                Father_Occupation=Father_Occupation,
                Mother_Occupation=Mother_Occupation,
                LocalGuardian_Ph=LocalGuardian_Ph,
                District=District,
                Pincode=Pincode,
                TenthSchoolName=TenthSchoolName,
                TenthPercentage=TenthPercentage,
                TenthPassoutYear=TenthPassoutYear,
                TwelthSchoolName=TwelthSchoolName,
                TwelthPercentage=TwelthPercentage,
                TwelthPassoutYear=TwelthPassoutYear,
                Keam=Keam,
                S_one=S_one,
                S_two=S_two,
                S_three=S_three,
                S_four=S_four,
                S_five=S_five,
                S_six=S_six,
                S_seven=S_seven,
                S_eight=S_eight,
                Current_CGPA=Current_CGPA,
                Supply_Count=Supply_Count,
                LinkedIn=LinkedIn,
                Internship=Internship
            )
            student_details.save()

        return redirect('form_details')

    else:
        # Retrieve the current user's student details if they exist
        student_details = StudentDetails.objects.filter(user=request.user).first()
    

    default_image_path = os.path.join(settings.STATIC_ROOT, 'default_image.jpg')

    if not student.image:
        # If the 'image' attribute has no file associated with it, use the default image path
        student.image = default_image_path
    context = {
        'student_details': student_details,
        'student': student,
    }
    return render(request, 'student_form.html', context)


@login_required(login_url='login')
@never_cache
def view_jobs(request):
    try:
        student = Student.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Handle case where student object does not exist
        return redirect('login')

    button_state = ButtonState.objects.first()
    applied_jobs = JobApplication.objects.filter(student=student).values_list('job', flat=True)
    jobs = Job.objects.exclude(id__in=applied_jobs)

    # Set a default image path
    default_image_path = os.path.join(settings.STATIC_ROOT, 'default_image.jpg')

    if not student.image:
        # If the 'image' attribute has no file associated with it, use the default image path
        student.image = default_image_path

    context = {
        'jobs': jobs,
        'student': student,
        'button_state': button_state,
    }

    return render(request, 'student_view_jobs.html', context)

@login_required(login_url='login')
@never_cache
def try_job(request, job_id):
    job = Job.objects.get(id=job_id)
    student = Student.objects.get(user=request.user)
    student_details = StudentDetails.objects.filter(user=request.user).first()

    if student_details is None:
        # Redirect to a page indicating that the form hasn't been filled
        return render(request, 'form_not_filled.html')

    if (
        student_details.Current_CGPA >= job.cgpa and
        student_details.Supply_Count <= job.Backpaper and
        student_details.TenthPercentage >= job.tenthper and
        student_details.TwelthPercentage >= job.twelthper and
        student_details.Internship >= job.internship
    ):
        # Check the number of existing job applications
        existing_applications = JobApplication.objects.filter(student=student).count()
        if existing_applications >= 3:
            # Display a prompt and deny the request
            return render(request, 'exceeded_applications.html')
        else:
            # Check if the student has already applied for the job
            existing_application = JobApplication.objects.filter(job=job, student=student).first()
            if existing_application:
                # Display a message that the student has already applied for the job
                messages.warning(request, 'You have already applied for this job.')
            else:
                # Create a new job application
                application = JobApplication(job=job, student=student, company=job.company)  # Set the company field
                application.save()
                # Display a success message
                messages.success(request, 'Job application submitted successfully.')
    else:
        # Redirect the user to the requirements_not_met page
        return render(request, 'requirements_not_met.html')

    return redirect('applied_jobs')



@login_required(login_url='login')
@never_cache
def applied_jobs(request):
    try:
        student = Student.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Handle case where student object does not exist
        return redirect('login')

    button_state = ButtonState.objects.first()
    jobs = Job.objects.all()
    applications = JobApplication.objects.filter(student=student)

    # Set a default image path
    default_image_path = os.path.join(settings.STATIC_ROOT, 'default_image.jpg')

    if not student.image:
        # If the 'image' attribute has no file associated with it, use the default image path
        student.image = default_image_path

    context = {
        'applications': applications,
        'student': student,
        'jobs': jobs,
        'button_state': button_state,
    }

    return render(request, 'student_applied_jobs.html', context)

@login_required(login_url='login')
@never_cache
def erase_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    application = JobApplication.objects.filter(job=job, student=request.user.student).first()
    if application:
        application.delete()
    return redirect('applied_jobs')

@login_required(login_url='login')
@never_cache
def company_details(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    jobs = company.job_set.all()  # Get all jobs associated with the company
    context = {
        'company': company,
        'jobs': jobs
    }
    return render(request, 'company_details.html', context)
