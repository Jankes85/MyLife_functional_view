from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Experience, Education, Course, Book, Skill


# Create your views here.


def intro(request):
    return render(request=request, template_name="aboutme/intro.html")


def about_me(request):
    return render(request=request, template_name="aboutme/aboutme.html")


def education(request):
    education = Education.objects.all()
    courses = Course.objects.all()
    books = Book.objects.all()
    ctx = {"education": education,
           "courses": courses,
           "books": books}
    return render(request=request, template_name="aboutme/education.html", context=ctx)


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
    skills = Skill.objects.all()
    skills_s = Skill.objects.filter(skill_type="s")
    skills_t = Skill.objects.filter(skill_type="t")
    ctx = {"skills_s": skills_s,
           "skills_t": skills_t}
    return render(request=request, template_name="aboutme/skills.html", context=ctx)


def experience(request):
    experience = Experience.objects.all()
    ctx = {"experience": experience}
    return render(request=request, template_name="aboutme/experience.html", context=ctx)


def interests(request):
    return render(request=request, template_name="aboutme/interests.html")


def blog(request):
    return render(request=request, template_name="aboutme/blog.html")


def thanks(request):
    return render(request=request, template_name="aboutme/thanks.html")
