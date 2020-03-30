from django.shortcuts import render


# Create your views here.

# for student homepage
def stu_home(request):
    return render(request, 'students/student_homepage.html')


# student to see courses
def stu_courses(request):
    return render(request, 'students/coursesSee.html')


# student to see after courses i.e contents
def stu_content(request):
    return render(request, 'students/student_seecontents.html')


# student to see after contents
def stu_topicinfo(request):
    return render(request, 'students/topic_info.html')

# see results
def see_results(request):
    return render(request, 'students/student_seeResults.html')

# student test
def stu_test(request):
    return render(request, 'students/student_test.html')