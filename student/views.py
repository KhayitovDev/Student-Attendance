from typing import Any
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, AttendanceRecord,Group
from django.views.generic import CreateView, DetailView, ListView
from .forms import AttendanceForm
from django.urls import reverse_lazy


def group_list(request):
    groups=Group.objects.all()
    context={'groups':groups}
    return render(request, 'groups.html', context)

def group_detail(request, pk):
    group=Group.objects.get(id=pk)
    context={'group':group}
    return render(request, 'group_detail.html', context)

class AttendanceListView(ListView):
    template_name='records.html'
    context_object_name='attendance_records'

    def get_queryset(self):
        group_id=self.kwargs.get('group_id')
        return AttendanceRecord.objects.filter(group_id=group_id)
    

class AttendanceCreateView(CreateView):
    model=AttendanceRecord
    form_class=AttendanceForm
    template_name='attendance.html'
    success_url=reverse_lazy('group_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        group_id = self.kwargs.get('group_id')
        kwargs['group_id'] = group_id
        return kwargs

    

 


    


    

