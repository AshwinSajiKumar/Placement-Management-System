from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Staff

class StaffInline(admin.StackedInline):
    model = Staff
    can_delete = False
    verbose_name_plural = 'Staff'

class CustomUserAdmin(UserAdmin):
    inlines = (StaffInline, )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
