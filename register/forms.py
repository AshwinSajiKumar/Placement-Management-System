from django import forms
from django.contrib.auth.models import User
from .models import Student

class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    branch = forms.ChoiceField(choices=Student.BRANCH_CHOICES, widget=forms.Select)

    class Meta:
        model = Student
        fields = ['admission_no', 'branch', 'StdEmail', 'image']


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['image']



class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='CSV File')

