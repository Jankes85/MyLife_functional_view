from datetime import datetime, date, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from calendar import HTMLCalendar

from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    model = Blog
    template_name = 'blog/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


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
    #     blog_l.append(blog)
    #     blog = Blog.objects.filter(creation_time__date=day)




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

