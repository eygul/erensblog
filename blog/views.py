from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Blog


def home(request, blog_id=None):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/home.html', context)

def blog(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return HttpResponse("This blog does not exist.", status=404)
    blogs = Blog.objects.all()
    context = {'blog': blog, 'blogs':blogs}
    return render(request, 'blog/blog.html', context)

def login(request):
    return render(request, 'blog/login.html')