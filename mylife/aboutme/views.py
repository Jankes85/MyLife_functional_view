import time

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def intro(request):
    return render(request=request, template_name="aboutme/intro.html")

def about_me(request):
    return render(request=request, template_name="aboutme/aboutme.html")

def education(request):
    return render(request=request, template_name="aboutme/education.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # Wyślij maila, zapisz do pliku, zapisz do bazy
            return redirect("thanks")
    else:
        form = ContactForm()

    ctx = {"form": form}
    return render(request=request, template_name="aboutme/contact.html", context=ctx)

def skills(request):
    return render(request=request, template_name="aboutme/skills.html")

def experience(request):
    return render(request=request, template_name="aboutme/experience.html")

def interests(request):
    return render(request=request, template_name="aboutme/interests.html")

def blog(request):
    return render(request=request, template_name="aboutme/blog.html")

def thanks(request):
    return render(request=request, template_name="aboutme/thanks.html")


