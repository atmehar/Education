from django.shortcuts import render, get_object_or_404, redirect
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'app1/home.html', {'students': students})


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'app1/student_detail.html', {'student': student})


def add_student(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        age = request.POST.get('age')
        course = request.POST.get('course')
        address = request.POST.get('address')

        Student.objects.create(
            full_name=full_name,
            roll_number=roll_number,
            email=email,
            age=age,
            course=course,
            address=address,
        )

        return redirect('home')

    return render(request, 'app1/add_student.html')
