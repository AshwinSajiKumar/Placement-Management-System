from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['slots', 'role', 'cgpa', 'Backpaper', 'Lpa', 'internship', 'tech', 'City', 'Country', 'tenthper', 'twelthper']