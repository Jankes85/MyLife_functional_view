from datetime import datetime, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from calendar import HTMLCalendar
from .models import Blog


def blank(request):
    return render(request=request, template_name="blog/blank.html")


def calendar_current(request):
    month = datetime.now().month
    year = datetime.now().year
    cal = HTMLCalendar().formatmonth(year, month)
    days = []
    for i in range(1, 32):
        try:
            day = date(int(year), int(month), int(i))
            days.append(day)
        except ValueError:
            break

    blog = Blog.objects.all()

    # blog_l = []
    # for day in days:
    #     blog = Blog.objects.filter(creation_time__date=day)
    #     blog_l.append(blog)

    # dict = [{k: v} for k, v in zip(days, blog_l)]


    prev = None
    next = None

    if month > 1:
        prev = f'{year}/{month - 1}'
    elif month == 1:
        prev = f"{year - 1}/{month + 11}"

    if month < 12:
        next = f'{year}/{month + 1}'
    elif month == 12:
        next = f"{year + 1}/{month - 11}"


    ctx = {"year": year,
           "month": month,
           "cal": cal,
           "prev": prev,
           "next": next,
           "days": days,
           "blog:": blog,
           }
    return render(request=request, template_name="blog/calendar_current.html", context=ctx)

def calendar_change(request, year, month):
    month = month
    year = year
    cal = HTMLCalendar().formatmonth(year, month)
    days = []
    for i in range(1, 32):
        try:
            day = date(int(year), int(month), int(i))
            days.append(day)
        except ValueError:
            break


    prev = None
    next = None

    if month > 1:
        prev = f'{year}/{month-1}'
    elif month == 1:
        prev = f"{year -  1}/{month + 11}"

    if month < 12:
        next = f'{year}/{month+1}'
    elif month == 12:
        next = f"{year +  1}/{month - 11}"

    ctx = {"year": year,
           "month": month,
           "cal": cal,
           "prev": prev,
           "next": next,
           "days": days}
    return render(request=request, template_name="blog/calendar_change.html", context=ctx)

