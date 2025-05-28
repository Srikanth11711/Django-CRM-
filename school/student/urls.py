from django.urls import path
from . import views

urlpatterns = [
    path('allstudents/', views.student_list, name='allstudents'),
    path('addstudent/', views.add_student, name="addstudent"),
    path('deletestudent/<str:id>/', views.delete, name="delete"),
    path('editstudent/<str:id>/', views.update_student, name="edit"),
    path('delete-selectedstudent/', views.delete_selected_students, name='delete_selected_students'),
]
