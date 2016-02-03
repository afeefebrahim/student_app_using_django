from django.contrib import admin
from .models import student
from student_app.models import UserProfile
# Register your models here.

admin.site.register(student)
admin.site.register(UserProfile)
