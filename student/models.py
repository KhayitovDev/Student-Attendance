from django.db import models
from django.utils import timezone

class Group(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class AttendanceRecord(models.Model):
    student = models.ManyToManyField(Student)
    group=models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    is_absent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.group.title} | {self.date}"
