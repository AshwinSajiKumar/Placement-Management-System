# Generated by Django 4.2.2 on 2023-06-27 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=20)),
                ('phno', models.IntegerField()),
                ('PEmailId', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('Dob', models.DateField()),
                ('Aadhar', models.IntegerField()),
                ('Pan', models.CharField(max_length=20)),
                ('Passport', models.CharField(max_length=20)),
                ('BloodGrp', models.CharField(max_length=10)),
                ('Religion', models.CharField(max_length=20)),
                ('Fathers_Name', models.CharField(max_length=20)),
                ('Mothers_Name', models.CharField(max_length=20)),
                ('Father_Occupation', models.CharField(max_length=20)),
                ('Mother_Occupation', models.CharField(max_length=20)),
                ('LocalGuardian_Ph', models.IntegerField()),
                ('District', models.CharField(max_length=20)),
                ('Pincode', models.IntegerField()),
                ('TenthSchoolName', models.CharField(max_length=50)),
                ('TenthPercentage', models.IntegerField()),
                ('TenthPassoutYear', models.IntegerField()),
                ('TwelthSchoolName', models.CharField(max_length=50)),
                ('TwelthPercentage', models.IntegerField()),
                ('TwelthPassoutYear', models.IntegerField()),
                ('Keam', models.IntegerField()),
                ('S_one', models.IntegerField(blank=True, default=None, null=True)),
                ('S_two', models.IntegerField(blank=True, default=None, null=True)),
                ('S_three', models.IntegerField(blank=True, default=None, null=True)),
                ('S_four', models.IntegerField(blank=True, default=None, null=True)),
                ('S_five', models.IntegerField(blank=True, default=None, null=True)),
                ('S_six', models.IntegerField(blank=True, default=None, null=True)),
                ('S_seven', models.IntegerField(blank=True, default=None, null=True)),
                ('S_eight', models.IntegerField(blank=True, default=None, null=True)),
                ('Current_CGPA', models.IntegerField(blank=True, null=True)),
                ('Supply_Count', models.IntegerField()),
                ('LinkedIn', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('Internship', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': "Student's Information",
            },
        ),
    ]
