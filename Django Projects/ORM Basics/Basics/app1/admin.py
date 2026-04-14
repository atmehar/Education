from django.contrib import admin
from .models import Course, Student, Assignment, Submission
# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Submission)
