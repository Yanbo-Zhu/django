from datetime import datetime

from django.shortcuts import HttpResponse
from .models import User, Article

# Create your views here.
def article_test(request):
    # user = User(username='知了', password='111111')
    # user.save()
    # article = Article(title='ChatGpt5已经发布啦！', content='xxx', author=user)
    # article.save()
    article = Article.objects.first()
    return HttpResponse(article.author.username)


def one_to_many(request):
    user = User.objects.first()
    articles = user.articles.filter(title__contains='XX').all()
    for article in articles:
        print(article.title)
    return HttpResponse("成功！")


def query1(reqeust):
    # article = Article.objects.filter(id__exact=1)
    # 查询结果.query看到，article.query，就可以看到底层执行的sql语句
    article = Article.objects.filter(title__iexact='chatgpt5已经发布啦！')
    print(article.query)
    print(article)
    return HttpResponse("xx")


def query2(request):
    # article = Article.objects.filter(title__contains='chat')
    article = Article.objects.filter(title__icontains='chat')
    print(article.query)
    print(article)
    return HttpResponse('query2')



def query3(request):
    # article = Article.objects.filter(title__contains='chat')
    article = Article.objects.filter(id__in=[1,2,3])
    print(article.query)
    print(article)
    return HttpResponse('query3')


def query4(request):
    # article = Article.objects.filter(title__contains='chat')
    start_date = datetime(year=2024, month=4, day=1)
    end_date = datetime(year=2024, month=4, day=2)
    article = Article.objects.filter(pub_time__range=(start_date, end_date))
    print(article.query)
    print(article)
    return HttpResponse('query4')


def query5(request):
    # 查找标题中，包含chat的文章的用户
    user = User.objects.filter(articles__title__icontains='chat')
    print(user.query)
    print(user)
    return HttpResponse('query5')

