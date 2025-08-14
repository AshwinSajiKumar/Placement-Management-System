from django.db import models
from django.contrib.auth.models import User
from staff_app.models import Staff

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    BRANCH_CHOICES = [
        ("CSE", 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('EEE', 'Electrical and Electronic Engineering'),
        ('IT', 'Information Technology'),
        ('CE', 'Civil Engineering'),
        ('AIDS', 'Artificial Intelligence and Data Science'),
        ('AEI', 'Applied Electronics & Instrumentation Engineering'),
    ]
    branch = models.CharField(max_length=4, choices=BRANCH_CHOICES, null=True, default='Unknown')
    admission_no = models.CharField(max_length=50, blank=True, null=True)
    StdEmail = models.EmailField(max_length=255)
    image = models.FileField(upload_to='student_images', blank=True, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='students', null=True)
    


class Stats(models.Model):
    labels = models.CharField(max_length=10)
    data = models.IntegerField()
    color = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'PIE & GRAPH'
