"""BTES_Academics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Created by me for students urls

from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.stu_home2, name="student_homepage"),
    path('<int:pk>/', views.stu_home, name="student_homepage"),
    path('<int:pk>/studentCourses', views.stu_courses, name="studentCourses"),
    path('<int:pk>/studentDiscussion', views.discussStudent, name="studentDiscussion"),
    path('<int:pk>/studentSeeContent/<str:info>/', views.stu_content, name="studentSeeContent"),
    path('<int:pk>/myInfo', views.myInfo, name="myInfo"),
    path('studentResults', views.see_results, name="studentResults"),
    path('<int:pk>/student_topicsInfo/<str:info>/<str:topic>/', views.stu_topicinfo, name="student_topicsInfo"),
    path('student_test', views.stu_test, name="student_test"),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='students/password_change_done.html'),
         name='password_change_done'),

    path('<int:pk>/password_change/', auth_views.PasswordChangeView.as_view(template_name='students/password_change.html'),
         name='password_change'),

]
