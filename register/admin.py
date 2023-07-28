from django.contrib import admin
from .models import Student,Stats

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'admission_no', 'StdEmail')
    list_filter = ('branch',)  # Add the 'branch' field as a filter  # Add the import_students function as an action

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            branch = request.user.staff.branch
            qs = qs.filter(branch=branch)
        return qs
    
class StatAdmin(admin.ModelAdmin):
    list_display = ('labels',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Stats,StatAdmin)