from django.contrib.auth.models import User
from django.db import models


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BRANCH_CHOICES = [
        ("CSE", 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('EEE', 'Electrical and Electronic Engineering'),
        ('IT', 'Information Technology'),
        ('CE', 'Civil Engineering'),
        ('AIDS', 'Artificial Intelligence and Data Science'),
        ('AEI', 'Applied Electronics & Instrumentation Engineering'),
        ('None','Company'),
    ]
    branch = models.CharField(max_length=4, choices=BRANCH_CHOICES, null=True, default='Unknown')
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
