from django import forms
from .models import AttendanceRecord, Student

class AttendanceForm(forms.ModelForm):
      class Meta:
          model=AttendanceRecord
          fields=[  'date', 'group', 'student', 'is_present']
          

      

       
       

   

