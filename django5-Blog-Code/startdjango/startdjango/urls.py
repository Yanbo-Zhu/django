"""
URL configuration for startdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse
from book import views
from django.urls import reverse

# https://www.baidu.com/s?wd=python
# URL与视图的映射
# /s(URL) -> 视图函数，进行映射
# http://127.0.0.1:8000  -> 返回“欢迎来到知了课堂”

def index(request):
    # print(reverse("book_detail_query_string"))
    # /book/str/1
    # print(reverse("book_str", kwargs={"book_id": 1}))

    # /book?id=1：如果是查询字符串的方式传参，那么就只能通过字符串拼接的方式
    # print(reverse("book_detail_query_string") + "?id=1")

    print(reverse("movie:movie_list"))
    return HttpResponse("欢迎来到知了课堂!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path("s", index) #http://127.0.0.1:8000/s

    # http://127.0.0.1:8000/book?id=1
    path('book', views.book_detail_query_string, name="book_detail_query_string"),

    # http://127.0.0.1:8000/book/1
    # 在book_id前指定参数类型有两点好处：
    # 1. 以后在浏览器中，如果book_id输入的是一个非整形，那么会出现404错误：/book/abc
    # 2. 在视图函数中，得到的book_id就是一个整形，否则，默认是str类型
    path('book/<int:book_id>', views.book_detail_path),
    path('book/str/<str:book_id>', views.book_str, name='book_str'),
    path("book/slug/<slug:book_id>", views.book_slug, name='book_slug'),
    path("book/path/<path:book_id>", views.book_path, name='book_path'),

    path('movie/', include("movie.urls"))
]
