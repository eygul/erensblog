from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<int:blog_id>/', views.blog, name="blog"),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
]