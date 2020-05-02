from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from Details.models import Course
from .forms import FileForm, ChangeFileForm, CommentForm
from students.models import Student
import csv, io
from .filters import StudentFilter
import pandas as pd


# Create your views here.
@login_required(login_url='/')
def home(request, pk):
    username = None
    context = {}
    if request.user.is_authenticated:
        username = request.user.username
        # instructor1 = Instructor.objects.get(id=pk)
        # print(instructor1)
        tid = request.user.instructor.id
        print(tid)
        context = {'username': username, 'instructor1': tid}
    return render(request, 'instructor/instructor_homepage.html', context)


@login_required(login_url='/')
def home1(request):
    username = None
    context = {}
    if request.user.is_authenticated:
        username = request.user.username
        # instructor1 = Instructor.objects.get(id=pk)
        # print(instructor1)
        tid = request.user.instructor.id
        print(tid)
        context = {'username': username, 'instructor1': tid}
    return render(request, 'instructor/instructor_homepage.html', context)


# upload contents
@login_required(login_url='/')
def uploadContents(request, pk):
    tid = request.user.instructor.id
    form = FileForm()
    inst = Instructor.objects.filter(id=tid)
    cs = {}
    for i in inst:
        c = i.course.id
        cs = Course.objects.filter(id=c)

    prompt = 'order of the csv file should be Question, Options1, Options2, Options3, Options4, Correct_Option, Explanation'

    if request.method == 'GET':
        context = {'form': form, 'instructor1': tid, 'course': cs, 'prompt': prompt}
        return render(request, 'instructor/upload_contents.html', context)

    if request.method == 'POST':
        form = FileForm(request.POST or None, request.FILES or None)
        print(form.errors)
        csv_file = request.FILES['qzfile']
        if form.is_valid() and csv_file.name.endswith('.csv'):
            data_set = csv_file.read().decode('UTF-8')
            form.save()
            csn = form.cleaned_data['courseName']
            tp = form.cleaned_data['topic']
            topics = FileUpload.objects.get(topic=tp)
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, quotechar='"', delimiter=',',
                                     quoting=csv.QUOTE_ALL, skipinitialspace=True):
                _, created = QuizUpload.objects.update_or_create(
                    courseName=csn,
                    topicName=topics,
                    Question=column[0],
                    optionA=column[1],
                    optionB=column[2],
                    optionC=column[3],
                    optionD=column[4],
                    correctOption=column[5],
                    explanation=column[6]
                )

            return HttpResponseRedirect('editContents/' + csn.courseName)
    context = {'form': form, 'instructor1': tid, 'course': cs}
    return render(request, 'instructor/upload_contents.html', context)


# See Courses
@login_required(login_url='/')
def seeContents(request, pk):
    user = request.user.username
    teacher = request.user.instructor.pk
    tid = request.user.instructor.id
    inst = Instructor.objects.filter(id=tid)
    cs = {}
    for i in inst:
        c = i.course.id
        print(c)
        cs = Course.objects.filter(id=c)
        print(cs)

    context = {'courses': cs, 'instructor1': tid}
    return render(request, 'instructor/Instructor_coursesSee.html', context)


# See contents
@login_required(login_url='/')
def editContents(request, pk, info):
    username = request.user.username
    tid = request.user.instructor.id
    courses = Course.objects.filter(courseName=info)
    cs1 = FileUpload.objects.filter(courseName_id=courses[0].id)
    context = {'username': username, 'instructor1': tid, 'courses': cs1}
    return render(request, 'instructor/edit_contents.html', context)


# edit contents
@login_required(login_url='/')
def changeContents(request, pk, pid):
    tid = request.user.instructor.id
    f = FileUpload.objects.get(id=pid)
    form = ChangeFileForm(instance=f)
    if request.method == "POST":
        form = ChangeFileForm(request.POST, instance=f)
        if form.is_valid():
            form.save()
            return editContents(request, tid, f.courseName.courseName)
    context = {'instructor1': tid, 'form': form}
    return render(request, 'instructor/upload_contents.html', context)


# delete contents
@login_required(login_url='/')
def deleteContents(request, pk, pid):
    tid = request.user.instructor.id
    f = FileUpload.objects.get(id=pid)
    inst = Instructor.objects.filter(id=tid)
    cs = {}
    for i in inst:
        c = i.course.id
        cs = Course.objects.filter(id=c)
    st = None
    for i in cs:
        st = i.courseName

    if request.method == "POST":
        print("III")
        f.delete()
        return redirect('editContents', pk=tid, info=f.courseName.courseName)
    context = {'instructor1': tid, 'study': f, 'cs': st}
    return render(request, 'instructor/delete_content.html', context)


# discussion
@login_required(login_url='/')
def discussInst(request, pk):
    sid = request.user.instructor.id
    inst = Instructor.objects.filter(id=sid)
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
            return redirect('discussInfo', pk=sid)
        else:
            print(comment_form.errors)
    else:
        comment_form = CommentForm()
    context = {'instructor1': sid, 'comments': comments, 'forms': comment_form}
    return render(request, 'instructor/discussionInstructor.html', context)




# make Test
def makeTest(request, pk):
    username = request.user.username
    tid = request.user.instructor.id
    context = {'username': username, 'instructor1': tid}
    return render(request, 'instructor/MakeTest.html', context)


# students info
@login_required(login_url='/')
def stu_Info(request, pk):
    username = request.user.username
    tid = request.user.instructor.id
    students = Student.objects.filter(instructor_id=tid)
    myfilter = StudentFilter(request.GET, queryset=students)
    print(myfilter)
    students = myfilter.qs
    context = {'username': username, 'instructor1': tid, 'students': students, 'myfilter': myfilter}
    return render(request, 'instructor/students_info.html', context)


# results
def stu_Results(request, pk):
    username = request.user.username
    tid = request.user.instructor.id
    context = {'username': username, 'instructor1': tid}
    return render(request, 'instructor/students_results.html', context)
