
from django.urls import path
from . import views

urlpatterns = [
  path('',  views.show_students),
  path('reg-user/', views.reg_student, name='reg_student'),
  path('show-students/', views.show_students, name='show_students'),
]

