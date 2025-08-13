from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from register.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import csv
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('student_import:student_list')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'student_import/login.html', {'error_message': error_message})

    return render(request, 'student_import/login.html')


def logout_view(request):
    logout(request)
    return redirect('student_import:csvlogin')

def student_list_view(request):
    students = Student.objects.all().order_by('-id')  # Order by the 'id' field in descending order
    return render(request, 'student_import/student_list.html', {'students': students})


@login_required
def csv_import_view(request):
    if request.method == 'POST':
        try:
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

            # Skip the header row
            next(csv_data)

            for row in csv_data:
                username = row[0]
                password = row[1]
                first_name = row[2]
                last_name = row[3]
                branch = row[4]
                admission_no = row[5]
                std_email = row[6]

                # Create a new user
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name)

                # Create a new student linked to the user
                student = Student(user=user, branch=branch, admission_no=admission_no, StdEmail=std_email)
                student.save()

            messages.success(request, 'Students imported successfully.')
            return redirect('student_import:student_list')
        except Exception as e:
            messages.error(request, f'Error importing CSV file: {str(e)}')
            return redirect('student_import:csv_import')

    return render(request, 'student_import/csv_import.html')