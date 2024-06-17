from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "index.html")


def baidu(request):
    return render(request, "baidu.html")


def info(request):
    # 1. 普通的变量
    username = '知了课堂'
    # 2. 字典类型
    book = {'name': "水浒传", 'author': '施耐庵'}
    # 3. 列表
    books = [
        {'name': "水浒传", 'author': '施耐庵'},
        {'name': "三国演义", 'author': '罗贯中'}
    ]
    # 4. 对象
    class Person:
        def __init__(self, realname):
            self.realname = realname
    context = {
        'username': username,
        'book': book,
        'books': books,
        'person': Person("知了课堂")
    }
    return render(request, 'info.html', context=context)


def if_view(request):
    age = 18
    return render(request, 'if.html', context={'age': age})


def for_view(request):
    # 1. 列表
    books = [
        # {'name': "水浒传", 'author': '施耐庵'},
        # {'name': "三国演义", 'author': '罗贯中'}
    ]
    # 2. 字典
    person = {
        'realname': "知了课堂",
        "age": 18,
        "height": 180
    }
    # for x in person.items/keys/values
    # break/continue：在模板中，不存在break和continue
    context = {
        'books': books,
        'person': person
    }
    return render(request, 'for.html', context)

def with_view(request):
    context = {
        'books': [
            {'name': "水浒传", 'author': '施耐庵'},
            {'name': "三国演义", 'author': '罗贯中'}
        ]
    }
    return render(request, 'with.html', context=context)


def url_view(request):
    return render(request, 'url.html')


def book_detail(request, book_id):
    return HttpResponse(f'您访问的图书id是：{book_id}')


def filter_view(request):
    greet = "Hello World, Hello Django"
    context = {
        "greet": greet,
        'birthday': datetime.now(),
        'profile': "xxx",
        'html': "<h1>欢迎来到知了课堂！</h1>"
    }
    return render(request, "filter.html", context=context)


def template_form(request):
    context = {
        'articles': ['小米su7', 'ChatGPT 5发布']
    }
    return render(request, "xfz_index.html", context=context)


def static_view(request):
    return render(request, 'static.html')