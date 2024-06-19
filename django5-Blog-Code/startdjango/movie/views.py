from django.shortcuts import render, HttpResponse


def movie_list(request):
    return HttpResponse("电影列表")


def movie_detail(request, movie_id):
    return HttpResponse(f"您获取的电影id是：{movie_id}")


