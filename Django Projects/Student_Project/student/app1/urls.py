from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='home'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path('add_student/', views.add_student, name='add_student'),
]