from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<int:blog_id>/', views.blog, name="blog"),
    path('login/', views.login, name='login'),
]