from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Experience, Education, Course, Book, Skill, Language
from django.core.mail import send_mail, BadHeaderError

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
            subject = form.cleaned_data["subject"]
            request.session["first_name"] = form.cleaned_data["first_name"]
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("thanks")
    else:
        form = ContactForm()

    ctx = {"form": form}
    return render(request=request, template_name="aboutme/contact.html", context=ctx)


def skills(request):
    skills_s = Skill.objects.filter(skill_type="s")
    skills_t = Skill.objects.filter(skill_type="t")
    languages = Language.objects.all()
    ctx = {"skills_s": skills_s,
           "skills_t": skills_t,
           "languages": languages}
    return render(request=request, template_name="aboutme/skills.html", context=ctx)


def experience(request):
    experience = Experience.objects.all()
    ctx = {"experience": experience}
    return render(request=request, template_name="aboutme/experience.html", context=ctx)


def thanks(request):
    ctx = {"first_name": request.session["first_name"]}
    return render(request=request, template_name="aboutme/thanks.html", context=ctx)


def python(request):
    education = Education.objects.filter(competences__icontains="python")
    courses = Course.objects.filter(competences__icontains="python")
    books = Book.objects.filter(competences__icontains="python")
    ctx = {"education": education,
           "courses": courses,
           "books": books,
           "skill": "Python",
           }
    return render(request=request, template_name="aboutme/from_where_skills.html", context=ctx)


def sql(request):
    education = Education.objects.filter(competences__icontains="sql")
    courses = Course.objects.filter(competences__icontains="sql")
    books = Book.objects.filter(competences__icontains="sql")
    ctx = {"education": education,
           "courses": courses,
           "books": books,
           "skill": "SQL",
           }
    return render(request=request, template_name="aboutme/from_where_skills.html", context=ctx)


def django(request):
    education = Education.objects.filter(competences__icontains="django")
    courses = Course.objects.filter(competences__icontains="django")
    books = Book.objects.filter(competences__icontains="django")
    ctx = {"education": education,
           "courses": courses,
           "books": books,
           "skill": "Django",
           }
    return render(request=request, template_name="aboutme/from_where_skills.html", context=ctx)


def html(request):
    education = Education.objects.filter(competences__icontains="html")
    courses = Course.objects.filter(competences__icontains="html")
    books = Book.objects.filter(competences__icontains="html")
    ctx = {"education": education,
           "courses": courses,
           "books": books,
           "skill": "HTML",
           }
    return render(request=request, template_name="aboutme/from_where_skills.html", context=ctx)


def css(request):
    education = Education.objects.filter(competences__icontains="css")
    courses = Course.objects.filter(competences__icontains="css")
    books = Book.objects.filter(competences__icontains="css")
    ctx = {"education": education,
           "courses": courses,
           "books": books,
           "skill": "CSS",
           }
    return render(request=request, template_name="aboutme/from_where_skills.html", context=ctx)


def js(request):
    education = Education.objects.filter(competences__icontains="javascript")
    courses = Course.objects.filter(competences__icontains="javascript")
    books = Book.objects.filter(competences__icontains="javascript")
    ctx = {"education": education,
           "courses": courses,
           "books": books,
           "skill": "JavaScript",
           }
    return render(request=request, template_name="aboutme/from_where_skills.html", context=ctx)