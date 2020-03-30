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
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='instructorHome'),
    path('uploadContents', views.uploadContents, name='uploadContents'),
    path('editContents', views.editContents, name='editContents'),
    path('seeContents', views.seeContents, name='seeContents'),
    path('stuInfo', views.stu_Info, name='stuInfo'),
    path('stuResults', views.stu_Results, name='stuResults'),
    path('makeTest', views.makeTest, name='makeTest'),
]
