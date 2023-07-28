from django.db import models
from django.contrib.auth.models import User
from register.models import Student


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='company_images', blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Company"

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    slots = models.IntegerField()
    role = models.CharField(max_length=30)
    cgpa = models.IntegerField()
    Backpaper = models.IntegerField()
    Lpa = models.IntegerField()
    internship = models.IntegerField()
    tech = models.CharField(max_length=30)
    City = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)
    tenthper = models.IntegerField()
    twelthper = models.IntegerField()

    def __str__(self):
        return self.role


class JobApplication(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    STATUS_CHOICES=[
        ('ACCEPTED', 'Application Accepted'),
        ('REJECTED', 'Rejected'),
        ('ROUND2', 'Selected for 2nd Round'),
        ('ROUND3', 'Selected for 3rd Round'),
        ('ROUND_Final', 'Selected for Final Round'),
        ('PLACED', 'Congrats!You are Placed'),
        ('Remove', 'You Failed to Clear'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='None')
    def __str__(self):
        return f"{self.student.user.username} applied for {self.job.role}"
