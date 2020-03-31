from django.shortcuts import render
from students.models import Student
from instructor.models import Instructor

def home(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/ContactUs.html')


def about(request):
    return render(request, 'main/AboutUs.html')


def login(request):
    print("In login")
    if request.method == "POST":
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]

        student = Student.objects.filter(email=uname)
        instuctor = Instructor.objects.filter(email=uname)
        print(student)
        print(instuctor)
        if student is not None:
            stu = Student.objects.get(email=uname)
            if pwd == stu.pwd:
                context = {"student": student}
                return render(request, 'students/student_homepage.html', context)
        elif instuctor is not None:
            instruc = Instructor.objects.get(email=uname)
            if instruc.pwd == pwd:
                context = {"instructor": instuctor}
                return render(request, 'instructor/instructor_homepage.html', context)
        else:
            return render(request, 'main/index.html')
