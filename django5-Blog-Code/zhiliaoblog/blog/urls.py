from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/detail/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('blog/pub', views.pub_blog, name='pub_blog'),
    path('blog/comment/pub', views.pub_comment, name='pub_comment'),
    path('search', views.search, name='search')
]