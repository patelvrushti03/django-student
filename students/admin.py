from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'email', 'course']

admin.site.register(Student, StudentAdmin)