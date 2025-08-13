from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    uid=models.CharField(max_length=20)
    phno=models.IntegerField()
    PEmailId=models.EmailField(max_length=255)
    address=models.CharField(max_length=255)
    Dob=models.DateField()
    Aadhar=models.IntegerField()
    Pan=models.CharField(max_length=20)
    Passport=models.CharField(max_length=20)
    BloodGrp=models.CharField(max_length=10)
    Religion=models.CharField(max_length=20)
    Fathers_Name=models.CharField(max_length=20)
    Mothers_Name=models.CharField(max_length=20)
    Father_Occupation=models.CharField(max_length=20)
    Mother_Occupation=models.CharField(max_length=20) 
    LocalGuardian_Ph=models.IntegerField()
    District=models.CharField(max_length=20)
    Pincode=models.IntegerField()
    TenthSchoolName=models.CharField(max_length=50)
    TenthPercentage=models.IntegerField()
    TenthPassoutYear=models.IntegerField()
    TwelthSchoolName=models.CharField(max_length=50)
    TwelthPercentage=models.IntegerField()
    TwelthPassoutYear=models.IntegerField()
    Keam=models.IntegerField()
    S_one=models.IntegerField(null=True, blank=True,default=None)
    S_two=models.IntegerField(null=True, blank=True,default=None)
    S_three=models.IntegerField(null=True, blank=True,default=None)
    S_four=models.IntegerField(null=True, blank=True,default=None)
    S_five=models.IntegerField(null=True, blank=True,default=None)
    S_six=models.IntegerField(null=True, blank=True,default=None)
    S_seven=models.IntegerField(null=True, blank=True,default=None)
    S_eight=models.IntegerField(null=True, blank=True,default=None)
    Current_CGPA=models.IntegerField(null=True, blank=True)
    Supply_Count=models.IntegerField()
    LinkedIn=models.CharField(max_length=255,null=True, blank=True,default=None)
    Internship=models.IntegerField()

    class Meta:
        verbose_name_plural="Student's Information"
 
    def __str__(self):
        return self.user.username

class ButtonState(models.Model):
    is_hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="Button View"