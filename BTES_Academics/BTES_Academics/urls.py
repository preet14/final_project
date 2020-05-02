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
from django.conf import settings
from django.conf.urls.static import static
from students import views as v1
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='homepage'),
                  path('homep/', views.h, name='homep'),
                  path('contactUs/', views.contact, name='contactUs'),
                  path('aboutUs/', views.about, name='aboutUs'),
                  path('login/', views.Login, name='login'),
                  path('logout/', views.logoutUser, name='logout'),
                  path('password_reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(
                           template_name='main/password_reset_done.html'),
                       name='password_reset_done'),

                  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/change_password.html'),
                       name='password_reset_confirm'),

                  path('password_reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset_form.html'), name='password_reset'),

                  path('reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(
                           template_name='main/password_reset_complete.html'),
                       name='password_reset_complete'),
                  path('instructor/', include('instructor.urls')),
                  path('student/', include('students.urls'), name='student')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "BTES_Academics Admin"
admin.site.site_title = "BTES Admin Portal"
admin.site.index_title = "Welcome to BTES_Academics Portal"
