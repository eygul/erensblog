from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Blog
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy


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

class AddBlog(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'blog/addblog.html'
    form_class = BlogForm
    success_message = "Added Successfully"
    success_url = reverse_lazy('addblog')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)