from django.shortcuts import render,HttpResponse

# 在URL中携带参数
# 1. 通过查询字符串（query string）：https://www.baidu.com/s?wd=python&a=1&b=2
# 2. 在path中携带：http://127.0.0.1:8000/book/2

# 1. 查询字符串：http://127.0.0.1:8000/book?id=3&name=xx
def book_detail_query_string(request):
    # request.GET = {"id":3}
    book_id = request.GET.get('id')
    name = request.GET.get('name')
    return HttpResponse(f"您查找的图书id是：{book_id}, 图书名称是：{name}")


# http://127.0.0.1:8000/book/1
def book_detail_path(request, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")


def book_str(request, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")


def book_slug(request, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")


def book_path(request, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")

