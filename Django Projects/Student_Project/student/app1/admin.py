from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'roll_number', 'email', 'age','course', 'date_joined')
    search_fields = ('roll_number', 'course')