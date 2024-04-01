from django.urls import path
from . import views
from .views import AddBlog

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<int:blog_id>/', views.blog, name="blog"),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('addblog/', AddBlog.as_view(), name='addblog'),
]