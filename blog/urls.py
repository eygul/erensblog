from django.urls import path
from . import views
from .views import AddBlog, UpdateBlog, SearchResultsView

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<int:blog_id>/', views.blog, name="blog"),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('addblog/', AddBlog.as_view(), name='addblog'),
    path('deleteblog/<int:blog_id>/', views.deleteBlog, name="delete-blog"),
    path('updateblog/<int:blog_id>/', UpdateBlog.as_view(), name='updateblog'),
    path('search/', SearchResultsView.as_view(), name='search'),
]