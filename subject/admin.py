from django.contrib import admin

# Register your models here.

from .models import Subject, Student, Teacher

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)