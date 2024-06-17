from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('test', views.article_test, name='article_test'),
    path('onetomany', views.one_to_many, name='one_to_many'),
    path('query1', views.query1, name='query1'),
    path('query2', views.query2, name='query2'),
    path('query3', views.query3, name='query3'),
    path('query4', views.query4, name='query4'),
    path('query5', views.query5, name='query5'),
]
