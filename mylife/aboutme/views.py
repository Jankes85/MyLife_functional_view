from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def intro(request):
    return render(request=request, template_name="aboutme/intro.html")

def about_me(request):
    return render(request=request, template_name="aboutme/aboutme.html")

def education(request):
    return render(request=request, template_name="aboutme/education.html")

def courses(request):
    return render(request=request, template_name="aboutme/courses.html")

def skills(request):
    return render(request=request, template_name="aboutme/skills.html")

def experience(request):
    return render(request=request, template_name="aboutme/experience.html")

def interests(request):
    return render(request=request, template_name="aboutme/interests.html")

def blog(request):
    return render(request=request, template_name="aboutme/blog.html")

