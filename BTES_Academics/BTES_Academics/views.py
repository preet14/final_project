from django.shortcuts import render


def home(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/ContactUs.html')


def about(request):
    return render(request, 'main/AboutUs.html')
