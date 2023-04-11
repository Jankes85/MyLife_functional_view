from datetime import datetime, date

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from calendar import HTMLCalendar
from .forms import BlogModelForm, BlogPostSearch
from .models import Blog


@login_required
def post_create(request):
    ctx = {'form': BlogModelForm(),
           'site_name': "Add post"}
    if request.method == "POST":
        form = BlogModelForm(request.POST)
        if form.is_valid():
            obj = Blog.objects.create(**form.cleaned_data)
            return redirect('post_detail', id=obj.id)
    else:
        form = BlogModelForm()

    return render(request=request, template_name='blog/create_post.html', context=ctx)


def post_edit(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = BlogModelForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.note = form.cleaned_data['note']
            post.entry_date = form.cleaned_data['entry_date']
            post.category = form.cleaned_data['category']
            post.author = form.cleaned_data['author']
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        initial = {'title': post.title, 'note': post.note, 'entry_date': post.entry_date, 'category': post.category,
                   'author': post.author}
        form = BlogModelForm(initial=initial)
        ctx = {'form': form,
               'site_name': "Edit post"}
    return render(request=request, template_name='blog/create_post.html', context=ctx)


def post_delete(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('calendar_current')
    ctx = {"post": post,
           'site_name': "Blog"}
    return render(request=request, template_name='blog/post_delete_form.html', context=ctx)


def blog_post_search(request):
    blog = Blog.objects.all()
    form = BlogPostSearch(request.GET)
    if form.is_valid():
        search_content = form.cleaned_data.get('search_content')
        if search_content:
            blog = blog.filter(Q(title__icontains=search_content)
                               | Q(note__icontains=search_content))

        entry_date_from = form.cleaned_data.get('entry_date_from')
        if entry_date_from:
            blog = blog.filter(entry_date__gte=entry_date_from)

        entry_date_to = form.cleaned_data.get('entry_date_to')
        if entry_date_to:
            blog = blog.filter(entry_date__lte=entry_date_to)

        category = form.cleaned_data.get('category')
        if category:
            blog = blog.filter(category__exact=category)

        author = form.cleaned_data.get('author')
        if author:
            blog = blog.filter(author__exact=author)

    form = BlogPostSearch()
    ctx = {'blog': blog,
           'form': form,
           'site_name': "Search"}
    return render(request=request, template_name='blog/search.html', context=ctx)


def post_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    ctx = {'post': post,
           'site_name': "Post"}
    return render(request=request, template_name='blog/post_details.html', context=ctx)


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
    blog_l = blog.filter(entry_date__gte=days[0], entry_date__lte=days[-1])


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
           'site_name': "Blog",
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
    blog_l = blog.filter(entry_date__gte=days[0], entry_date__lte=days[-1])

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
           'site_name': "Blog"
           }
    return render(request=request, template_name="blog/calendar_current.html", context=ctx)
