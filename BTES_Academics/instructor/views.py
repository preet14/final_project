from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'instructor/instructor_homepage.html')


# upload contents
def uploadContents(request):
    return render(request, 'instructor/upload_contents.html')


# See Contents
def seeContents(request):
    return render(request, 'instructor/Instructor_coursesSee.html')


# Edit contents
def editContents(request):
    return render(request, 'instructor/edit_contents.html')


# make Test
def makeTest(request):
    return render(request, 'instructor/MakeTest.html')


# students info
def stu_Info(request):
    return render(request, 'instructor/students_info.html')


# results
def stu_Results(request):
    return render(request, 'instructor/students_results.html')
