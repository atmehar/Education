from calendar import HTMLCalendar
from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Student, Assignment, Submission
from django.db.models import Count, Max, Avg
# Create your views here.
"""
def home(request):
    return HttpResponse("Hello, World!")

def course_list(request):
    courses = Course.objects.all()
    return HttpResponse(courses)

def student_list(request):
    students = Student.objects.all()
    return HttpResponse(students)

def assignment_list(request):
    assignments = Assignment.objects.all()
    return HttpResponse(assignments)

def submission_list(request):
    submissions = Submission.objects.all()
    return HttpResponse(submissions)
"""

def student_list(request):
    students = Student.objects.all()
    return render(request, 'app1/student_list.html', {'students': students})

def student_age(request):
    students = Student.objects.filter(age__gt=18)
    if students:
        student_names = " , ".join(s.name for s in students)
        return HttpResponse(f"Students older than 18: {student_names}")
    else:
        return HttpResponse("Students older than 18: (none found)")

def student_course_name(request):
    students = Student.objects.filter(course__name="Python")
    if students:
        student_names = " , ".join(s.name for s in students)
        return HttpResponse(f"Students in Python: {student_names}")
    else:
        return HttpResponse("Students in Python: (none found)")

def Assignment_of_a_Specific_Course(request):
    assignments = Assignment.objects.filter(course__name="Database")
    if assignments:
        assignment_titles = " , ".join(a.title for a in assignments)
        return HttpResponse(f"Assignments for Database: {assignment_titles}")
    else:
        return HttpResponse("Assignments for Database: (none found)")

def submissions_of_a_specific_student(request):
    submissions = Submission.objects.filter(student__name="Ali")
    if submissions:
        submission_marks = " , ".join(str(s.marks_obtained) for s in submissions)
        return HttpResponse(f"Submissions for Ali: {submission_marks}")
    else:
        return HttpResponse("Submissions for Ali: (none found)")

def count_students_in_each_course(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    if courses:
        lines = [f"{c.name}: {c.student_count}" for c in courses]
        return HttpResponse(f"Students per course: {' | '.join(lines)}")
    else:
        return HttpResponse("Students per course: (none found)")

def students_scored_more_than_80(request):
    students = Student.objects.filter(submission__marks_obtained__gt=70).distinct()
    if students:
        student_names = " , ".join(s.name for s in students)
        return HttpResponse(f"Students who scored more than 80 in any assignment: {student_names}")
    else:
        return HttpResponse("Students who scored more than 80: (none found)")

def students_who_have_not_submitted_specific_assignment(request):
    assignment = Assignment.objects.filter(course__name="Database").first()
    if assignment:
        students = Student.objects.exclude(submission__assignment=assignment).distinct()
        if students:
            student_names = " , ".join(s.name for s in students)
            return HttpResponse(f"Students who have not submitted '{assignment.title}': {student_names}")
        else:
            return HttpResponse(f"All students have submitted '{assignment.title}'")
    else:
        return HttpResponse("Assignment not found")

def students_ordered_by_age_desc(request):
    students = Student.objects.order_by('-age')
    if students:
        lines = [f"{s.name} ({s.age})" for s in students]
        return HttpResponse(f"Students by age (desc): {' | '.join(lines)}")
    else:
        return HttpResponse("Students by age: (none found)")

def top_3_students_in_assignment(request):
    assignment = Assignment.objects.filter(course__name="Database").first()
    if assignment:
        submissions = Submission.objects.filter(assignment=assignment).order_by('-marks_obtained')[:3]
        if submissions:
            lines = [f"{s.student.name}: {s.marks_obtained}" for s in submissions]
            return HttpResponse(f"Top 3 in '{assignment.title}': {' | '.join(lines)}")
        else:
            return HttpResponse(f"No submissions for '{assignment.title}'")
    else:
        return HttpResponse("Assignment not found")

def average_marks_per_student(request):
    students = Student.objects.annotate(avg_marks=Avg('submission__marks_obtained')).filter(avg_marks__isnull=False)
    if students:
        lines = [f"{s.name}: {s.avg_marks:.1f}" for s in students]
        return HttpResponse(f"Average marks per student: {' | '.join(lines)}")
    else:
        return HttpResponse("Average marks per student: (none found)")

def average_marks_per_course(request):
    courses = Course.objects.annotate(avg_marks=Avg('assignment__submission__marks_obtained')).filter(avg_marks__isnull=False)
    if courses:
        lines = [f"{c.name}: {c.avg_marks:.1f}" for c in courses]
        return HttpResponse(f"Average marks per course: {' | '.join(lines)}")
    else:
        return HttpResponse("Average marks per course: (none found)")

def highest_scorer_in_each_course(request):
    courses = Course.objects.annotate(
        top_marks=Max('student__submission__marks_obtained')
    ).filter(top_marks__isnull=False)
    result_lines = []
    for course in courses:
        top_student = Student.objects.filter(course=course).annotate(
            best=Max('submission__marks_obtained')
        ).filter(best=course.top_marks).first()
        if top_student:
            result_lines.append(f"{course.name}: {top_student.name} ({course.top_marks})")
    if result_lines:
        return HttpResponse(f"Highest scorer per course: {' | '.join(result_lines)}")
    else:
        return HttpResponse("Highest scorer per course: (none found)")

def students_who_failed(request):
    students = Student.objects.filter(submission__marks_obtained__lt=40).distinct()
    if students:
        student_names = " , ".join(s.name for s in students)
        return HttpResponse(f"Students who failed (marks < 40): {student_names}")
    else:
        return HttpResponse("Students who failed: (none found)")

def total_submissions_per_student(request):
    students = Student.objects.annotate(sub_count=Count('submission'))
    if students:
        lines = [f"{s.name}: {s.sub_count}" for s in students]
        return HttpResponse(f"Total submissions per student: {' | '.join(lines)}")
    else:
        return HttpResponse("Total submissions per student: (none found)")
