# attendance/admin.py

from django.contrib import admin
from .models import Student, Group, AttendanceRecord

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(AttendanceRecord)
