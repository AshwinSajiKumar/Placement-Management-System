from django.contrib import admin
from .models import Company,Job,JobApplication
from django.db import models
from django.forms import inlineformset_factory
# Register your models here.
class ApplicationInline(admin.TabularInline):
    model = JobApplication
    extra = 1

class JobAdmin(admin.ModelAdmin):
    inlines = (ApplicationInline,)
    list_display = ('role', 'slots', 'company_name')

    def company_name(self, obj):
        return obj.company.name  # Retrieve the company name for the job

    company_name.short_description = 'Company'

class CompanyAdmin(admin.ModelAdmin):
    inlines = (ApplicationInline,)
    list_display = ('name', 'applied_students')

    def applied_students(self, obj):
        students = obj.jobapplication_set.all()
        applied_students_list = []
        for application in students:
            student = application.student
            full_name = f"{student.user.first_name} {student.user.last_name}"
            branch = student.branch
            applied_students_list.append(f"{full_name} ({branch})")
        return ", ".join(applied_students_list)

    applied_students.short_description = 'Applied Students'

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'company_name', 'student_name', 'student_branch')

    def company_name(self, obj):
        return obj.job.company.name

    def student_name(self, obj):
        return f"{obj.student.user.first_name} {obj.student.user.last_name}"

    def student_branch(self, obj):
        return obj.student.branch

    company_name.short_description = 'Company'
    student_name.short_description = 'Student Name'
    student_branch.short_description = 'Branch'

admin.site.register(JobApplication, JobApplicationAdmin)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)