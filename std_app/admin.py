from django.contrib import admin
from .models import StudentDetails,ButtonState

class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_branch', 'uid', 'phno']  # Customize the displayed fields
    list_filter = ['user__student__branch']  # Add the 'branch' field as a filter

    def get_branch(self, obj):
        return obj.user.student.branch  # Retrieve the branch from the related Student model

    get_branch.short_description = 'Branch'  # Set a custom column header name

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            branch = request.user.staff.branch
            qs = qs.filter(user__student__branch=branch)
        return qs

admin.site.register(StudentDetails, StudentDetailsAdmin)


class ButtonStateAdmin(admin.ModelAdmin):
    list_display = ['get_button_name', 'is_hidden']
    list_editable = ['is_hidden']
    readonly_fields = [field.name for field in ButtonState._meta.get_fields() if field.name != 'id']
    list_display_links = None

    def has_add_permission(self, request):
        return False  # Disable the ability to add new objects

    def get_button_name(self, obj):
        return 'View'  # Replace 'Button' with the desired name for the objects

    get_button_name.short_description = 'Feature'

admin.site.register(ButtonState, ButtonStateAdmin)
