from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup_user,name="signup"),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name="logout"),
    
    path('allteachers/',views.teacher_list,name='allteachers'),
    path('add/',views.add_teacher,name="addTeacher"),
    path('delete/<str:id>',views.delete,name="delete"),
    path('edit/<str:id>',views.update_teacher,name="edit"),
    path('delete-selected/', views.delete_selected_teachers, name='delete_selected_teachers'),

]
