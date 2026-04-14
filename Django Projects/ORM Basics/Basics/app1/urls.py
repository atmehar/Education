from django.urls import path
from . import views

urlpatterns = [
    path('student_list/', views.student_list, name='student_list'),
    path('student_age/', views.student_age, name='student_age'),
    path('student_course_name/', views.student_course_name, name='student_course_name'),
    path('Assignment_of_a_Specific_Course/', views.Assignment_of_a_Specific_Course, name='Assignment_of_a_Specific_Course'),
    path('submissions_of_a_specific_student/', views.submissions_of_a_specific_student, name='submissions_of_a_specific_student'),
    path('count_students_in_each_course/', views.count_students_in_each_course, name='count_students_in_each_course'),
    path('students_scored_more_than_80/', views.students_scored_more_than_80, name='students_scored_more_than_80'),
    path('students_who_have_not_submitted_specific_assignment/', views.students_who_have_not_submitted_specific_assignment, name='students_who_have_not_submitted_specific_assignment'),
    path('students_ordered_by_age_desc/', views.students_ordered_by_age_desc, name='students_ordered_by_age_desc'),
    path('top_3_students_in_assignment/', views.top_3_students_in_assignment, name='top_3_students_in_assignment'),
    path('average_marks_per_student/', views.average_marks_per_student, name='average_marks_per_student'),
    path('average_marks_per_course/', views.average_marks_per_course, name='average_marks_per_course'),
    path('highest_scorer_in_each_course/', views.highest_scorer_in_each_course, name='highest_scorer_in_each_course'),
    path('students_who_failed/', views.students_who_failed, name='students_who_failed'),
    path('total_submissions_per_student/', views.total_submissions_per_student, name='total_submissions_per_student'),
]