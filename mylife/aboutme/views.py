from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def intro(request):
    return render(request=request, template_name="aboutme/intro.html")

def about_me(request):
    return HttpResponse("about me")

def education(request):
    return HttpResponse("education")

def courses(request):
    return HttpResponse("education")

def experience(request):
    return HttpResponse("work experience")

def interests(request):
    return HttpResponse("my interests")

