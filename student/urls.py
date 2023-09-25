from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_list, name='group_list'),
    path('group_detail/<int:pk>/', views.group_detail, name='group_detail'),
    path('attendance/<int:group_id>/', views.AttendanceCreateView.as_view(), name='take_attendance'),
    path('attendance-records/<int:group_id>/', views.AttendanceListView.as_view(), name='attendance_listview')
]
