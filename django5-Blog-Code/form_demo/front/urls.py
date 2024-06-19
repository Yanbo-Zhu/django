from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_view, name='regsiter'),
    path('article', views.article_view, name='article view')
]