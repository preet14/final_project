from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Student
from Details.models import *
from instructor.models import *
from django.core.paginator import Paginator
from .forms import CommentForm


# Create your views here.

# for student homepage
@login_required(login_url='/')
def stu_home(request, pk):
    if request.user.is_authenticated:
        username = request.user.username
        sid = request.user.student.id
        context = {'student1': sid}
    return render(request, 'students/student_homepage.html', context)


@login_required(login_url='/')
def stu_home2(request):
    if request.user.is_authenticated:
        username = request.user.username
        sid = request.user.student.id
        context = {'student1': sid}
    return render(request, 'students/student_homepage.html', context)


# student to see courses
@login_required(login_url='/')
def stu_courses(request, pk):
    sid = request.user.student.id
    inst = Student.objects.filter(id=sid)
    cs = {}
    for i in inst:
        c = i.course.id
        # print(c)
        cs = Course.objects.filter(id=c)
        # print(cs)
    context = {'courses': cs, 'student1': sid}
    return render(request, 'students/coursesSee.html', context)


# student to see after courses i.e contents
@login_required(login_url='/')
def stu_content(request, pk, info):
    sid = request.user.student.id
    # print(tid)
    courses = Course.objects.filter(courseName=info)
    cs1 = FileUpload.objects.filter(courseName_id=courses[0].id)
    posts = FileUpload.objects.filter(courseName_id=courses[0].id).order_by('id')
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'student1': sid, 'courses': cs1, 'info': info, 'posts': posts}
    return render(request, 'students/student_seecontents.html', context)


# student to see after contents
@login_required(login_url='/')
def stu_topicinfo(request, pk, info, topic):
    sid = request.user.student.id
    courses = Course.objects.filter(courseName=info)
    cs1 = FileUpload.objects.filter(courseName_id=courses[0].id)
    posts = FileUpload.objects.filter(courseName_id=courses[0].id).order_by('id')
    paginator = Paginator(posts, 1)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    s = None
    for p in posts:
        s = p.id
    print(s)

    flag = True
    qz = QuizUpload.objects.filter(topicName_id=s)
    if qz is None:
        flag = False

    context = {'student1': sid, 'info': info, 'posts': posts, 'quiz': qz, 'flag': flag}

    return render(request, 'students/topic_info.html', context)


# discussion
@login_required(login_url='/')
def discussStudent(request, pk):
    sid = request.user.student.id
    inst = Student.objects.filter(id=sid)
    cs = {}
    for i in inst:
        c = i.course.id
        cs = Course.objects.filter(id=c)
    temp = Course.objects.get(pk=cs[0].id)
    comments = Comment.objects.filter(course_id=cs[0].id, reply=None).order_by('-id')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content1 = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            cmt = Comment.objects.create(course=temp, user=request.user, content=content1, reply=comment_qs)
            cmt.save()
            return redirect('studentDiscussion', pk=sid)
        else:
            print(comment_form.errors)
    else:
        comment_form = CommentForm()
    context = {'student1': sid, 'comments': comments, 'forms': comment_form}
    return render(request, 'students/discussionStudent.html', context)


# my info
@login_required(login_url='/')
def myInfo(request, pk):
    sid = request.user.student.id
    stuinfo = Student.objects.filter(pk=sid)
    # for i in stuinfo:
    #     print(i.user.first_name)
    #     print(i.user.last_name)
    #     print(i.user.email)
    #     print(i.regId)
    #     print(i.instructor.user.first_name)
    #     print(i.instructor.user.email)
    context = {'student1': sid, 'stuinfo': stuinfo}
    return render(request, 'students/myInformation.html', context)


# see results
def see_results(request):
    return render(request, 'students/student_seeResults.html')


# student test
def stu_test(request):
    return render(request, 'students/student_test.html')
