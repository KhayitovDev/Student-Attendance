from django import forms
from .models import AttendanceRecord, Student

class AttendanceForm(forms.ModelForm):
    date = forms.DateField(label='Enter Date', widget=forms.DateInput(attrs={'class': 'form-control-lg', 'type': 'date'}))
    student = forms.ModelMultipleChoiceField(
        label='Students',
        queryset=Student.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-lg'}),
    )
    is_absent = forms.BooleanField(
        label='Is Absent',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'transform: scale(1.5);'}),
    )

    def __init__(self, group_id, *args, **kwargs):
        super(AttendanceForm, self).__init__( *args, **kwargs)
        self.fields['student'].queryset = Student.objects.filter(group_id=group_id)
        self.fields['group'].initial = group_id

    class Meta:
        model = AttendanceRecord
        fields = ['date','group', 'student', 'is_absent']



       
       

   

