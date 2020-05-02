from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from students.models import Student
from instructor.models import Instructor
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.conf import settings


def home(request):
    return render(request, 'main/index.html')


def h(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = StudentProfile(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('homepage')
        else:
            return HttpResponse('Data Not Saved')
    form = ExtendedUserCreationForm()
    profile_form = StudentProfile()
    # print(form,profile_form)
    context = {'form': form, 'profile_form': profile_form}

    return render(request, 'main/in2.html', context)


def contact(request):
    return render(request, 'main/ContactUs.html')


def about(request):
    return render(request, 'main/AboutUs.html')


def Login(request):
    print("In login")
    f = True
    context = {'f': f}
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        status = request.POST.get('status')
        print(settings.AUTHENTICATION_BACKENDS)
        user1 = authenticate(request, username=username, password=password)
        print(user1)
        if user1 is not None:
            form = login(request, user1)
            u1 = User.objects.get(username=user1.username)
            if status == "Instructor" and Instructor.objects.filter(user=u1):
                messages.success(request, f' wecome {username} !!')
                return HttpResponseRedirect('/instructor/')
            elif status == "Student" and Student.objects.filter(user=u1):
                std = Student.objects.get(user=u1)
                if std.active:
                    messages.success(request, f' wecome {username} !!')
                    return HttpResponseRedirect('/student/')
                else:
                    logout(request)
                    messages.info(request, 'account is not active')
                    return HttpResponseRedirect('/')
            else:
                messages.info(request, 'Account is not activated')
        else:
            messages.info(request, 'account dont exist or invalid credentials')
            return HttpResponseRedirect('/')

    else:
        return redirect('homepage')

    return render(request, 'main/index.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')
