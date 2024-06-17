

# 1 Project 

## 1.1 用命令行的方式：
1. 创建项目：打开终端，使用命令： django-admin startproject [项目名称] 即可创建。比如： django-admin startproject first_project 。
2. 创建应用（app）：一个项目类似于是一个架子，但是真正起作用的还是app 。在终端进入到项目所在的路径，然后执行python manage.py startapp [app名称] 创建一个app。


或者用 pycharm 可以直接创建 

命令: 
`django-admin.py startproject new_project_name`

django-admin startproject mysite

一个新建立的项目结构大概如下：
```
mysite/  
    manage.py  
    mysite/  
        __init__.py  
        settings.py  
        urls.py  
        asgi.py  
        wsgi.py  
```


## 1.2 运行Django项目

通过命令行的方式： 
- python manage.py runserver 。 这样可以在本地访问你的网站，默认端口号 是8000 ，这样就可以在浏览器中通过http://127.0.0.1:8000/ 来访问你的网站啦。
- 如果想要修改端口号，那么在运行的时候可以指定端口号， python manage.py runserver 9000 这样就可以 通过9000 端口来访问啦。
- 另外，这样运行的项目只能在本机上能访问，如果想要在其他电脑上也能访问本网站，那么需要指定ip 地址为0.0.0.0 。 示例为： python manage.py runserver 0.0.0.0:8000 。


通过pycharm 运行。直接点击右上角的绿色箭头按钮即可运行。



## 1.3 项目结构介绍

1. manage.py ：以后和项目交互基本上都是基于这个文件。一般都是在终端输入python manage.py [子命令] 。可以输入python manage.py help 看下能做什么事情。除非你知道你自己在做什么， 一般情况下不应该编辑这个文件。
2. settings.py ：本项目的设置项，以后所有和项目相关的配置都是放在这个里面。
3. urls.py ：这个文件是用来配置URL路由的。比如访问http://127.0.0.1/news/ 是访问新闻列表 页，这些东西就需要在这个文件中完成。
4. wsgi.py ：项目与WSGI 协议兼容的web 服务器入口，部署的时候需要用到的，一般情况下也是不 需要修改的。

# 2 Application

app 是django 项目的组成部分。一个app 代表项目中的一个模块，所有URL 请求的响应都是由app 来 处理。比如豆瓣，里面有图书，电影，音乐，同城等许许多多的模块，如果站在django 的角度来看，图 书，电影这些模块就是app ，图书，电影这些app 共同组成豆瓣这个项目。因此这里要有一个概念， django 项目由许多app 组成，一个app 可以被用到其他项目， django 也能拥有不同的app 。

通过命令： python manage.py startapp book 可以新造一个 app 出来 

python manage.py startapp polls

系统会自动生成 polls应用的目录，其结构如下：

```
polls/  
    __init__.py  
    admin.py  
    apps.py  
    migrations/  
        __init__.py  
    models.py  
    tests.py  
    views.py  
```




