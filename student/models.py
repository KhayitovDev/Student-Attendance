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
    IS_PRESENT='T'
    IS_NOT_PRESENT='F'
    CHOICES=[
        (IS_PRESENT, 'True'),
        (IS_NOT_PRESENT, 'False')
    ]
    student = models.ManyToManyField(Student)
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.CharField(max_length=1, choices=CHOICES, default=IS_NOT_PRESENT)

    def __str__(self):
        return f"{self.group.title}-{self.date}"
