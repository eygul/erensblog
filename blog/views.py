from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!!!!!')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            messages.error(request, 'Username or password does not exist.')
    context= {}
    return render(request, 'blog/login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('home')