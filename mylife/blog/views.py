from datetime import datetime, date
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from calendar import HTMLCalendar

from .forms import BlogModelForm
from .models import Blog


def post_create(request):
    if request.method == "POST":
        form = BlogModelForm(request.POST)
        if form.is_valid():
            pass
            obj = Blog.objects.create(**form.cleaned_data)
            return redirect('post_detail', id=obj.id)
    else:
        form = BlogModelForm()
    return render(request, 'blog/create_post.html', {'form': form})

def post_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    ctx = {'post': post}
    return render(request, 'blog/post_details.html', ctx)


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

    blog_l = []
    for day in days:
        blog_date = Blog.objects.filter(entry_date=day).values()
        blog_l.append(blog_date)

    date_blog_dict = [{k: v} for k, v in zip(days, blog_l)]


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
           "blog": blog,
           "blog_l": blog_l,
           "date_blog_dict": date_blog_dict,
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

    blog = Blog.objects.all()

    blog_l = []
    for day in days:
        blog_date = Blog.objects.filter(entry_date=day).values()
        blog_l.append(blog_date)


    date_blog_dict = [{k: v} for k, v in zip(days, blog_l)]

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
           "blog": blog,
           "blog_l": blog_l,
           "date_blog_dict": date_blog_dict,
           }
    return render(request=request, template_name="blog/calendar_current.html", context=ctx)

