from django.urls import path
from . import views

# 应用命名空间
app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_book, name='add_book'),
    path('query', views.query_book, name='query_book'),
    path('order', views.order_view, name='order_book'),
    path('update', views.update_view, name='update_book'),
    path('delete', views.delete_view, name='delete_book'),
    path('tag', views.book_tag, name='book_tag'),
]