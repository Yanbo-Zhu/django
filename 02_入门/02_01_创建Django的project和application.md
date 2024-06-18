

# 1 MTV模型


为了更好的理解Django5的应用配置，我们先来学习下Django的MTV模型。
Django的MTV分别代表：
Model(模型)：业务对象与数据库的对象(ORM)
Template(模版)：负责如何把页面展示给用户
View(视图)：负责业务逻辑，并在适当的时候调用Model和Template
此外，Django还有一个urls分发器，它的作用是将一个URI的页面请求分发给不同的view处理，view再调用相应的Model和Template。 Django WEB框架示意图如下所示:

![](images/Pasted%20image%2020240618232343.png)


# 2 Project 

## 2.1 用命令行的方式：
1. 创建项目：打开终端，使用命令： django-admin startproject [项目名称] 即可创建。比如： django-admin startproject first_project 。
2. 创建应用（app）：一个项目类似于是一个架子，但是真正起作用的还是app 。在终端进入到项目所在的路径，然后执行python manage.py startapp [app名称] 创建一个app。


或者用 pycharm 可以直接创建 

命令: 
`django-admin.py startproject new_project_name`

django-admin startproject mysite

# 3 新建立的项目结构

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

- manage.py :项目管理命令行工具，内置多种方式与项目进行交互，包括启动项目，创建app，数据管理等。在命令提示符窗口下，将路径切换 python222_site1项目并输入python manage.py
- help，可以查看该工具的指令信息；【不用修改】
- `__init__.py` ：初始化文件,一般情况下无须修改；
- settings.py ：项目的配置文件，项目的所有功能都需要在该文件中进行配置；
- urls.py ：项目的路由设置，设置网站的具体网址内容；
- wsgi.py ：全 称 为 Python Web Server Gateway Interface，即Python服务器⽹关接⼝，是Python应⽤与Web服务器之间的接⼝，⽤于Django项⽬在服务器上的部署和上线；【不用修改】
- asgi.py ：开启⼀个ASGI服务，ASGI是异步⽹关协议接⼝；【不用修改】

1. manage.py ：以后和项目交互基本上都是基于这个文件。一般都是在终端输入python manage.py [子命令] 。可以输入python manage.py help 看下能做什么事情。除非你知道你自己在做什么， 一般情况下不应该编辑这个文件。
2. settings.py ：本项目的设置项，以后所有和项目相关的配置都是放在这个里面。
3. urls.py ：这个文件是用来配置URL路由的。比如访问http://127.0.0.1/news/ 是访问新闻列表 页，这些东西就需要在这个文件中完成。
4. wsgi.py ：项目与WSGI 协议兼容的web 服务器入口，部署的时候需要用到的，一般情况下也是不 需要修改的。

## 3.1 运行Django项目

通过命令行的方式： 
- python manage.py runserver 。 这样可以在本地访问你的网站，默认端口号 是8000 ，这样就可以在浏览器中通过http://127.0.0.1:8000/ 来访问你的网站啦。
- 如果想要修改端口号，那么在运行的时候可以指定端口号， python manage.py runserver 9000 这样就可以 通过9000 端口来访问啦。
- 另外，这样运行的项目只能在本机上能访问，如果想要在其他电脑上也能访问本网站，那么需要指定ip 地址为0.0.0.0 。 示例为： python manage.py runserver 0.0.0.0:8000 。


通过pycharm 运行。直接点击右上角的绿色箭头按钮即可运行。



## 3.2 python manage.py help

![](images/Pasted%20image%2020240618232004.png)


指令说明
changepassword 修改内置用户表的用户密码
createsuperuser 为内置用户表创建超级管理员账号
remove_stale_contenttypes 删除数据库中已不使用的数据表
check 检测整个项目是否存在异常问题
compilemessages 编译语言文件，用于项目的区域语言设置
createcachetable 创建缓存数据表，为内置的缓存机制提供存储功能
dbshell 进入Django配置的数据库，可以执行数据库的SOL语句
diffsettings 显示当前settings.py的配置信息与默认配置的差异
dumpdata 导出数据表的数据并以JSON格式存储，如 python manage.py
dumpdata index >data.json，这是index的模型所对应的数据导 出，并保存在 data.json文件中
flush 清空数据表的数据信息
inspectdb 获取项目所有模型的定义过程
loaddata 将数据文件导入数据表，如 python manage.py loaddatadata.,json
makemessages 创建语言文件，用于项目的区域语言设置
makemigrations 从模型对象创建数据迁移文件并保存在App 的migrations文件夹
migrate 根据迁移文件的内容，在数据库里生成相应的数据表
sendtestemail 向指定的收件人发送测试的电子邮件
shell 进入Django的Shell模式,用于调试项目功能
showmigrations 查看当前项目的所有迁移文件
sqlflush 查看清空数据库的SOL语句脚本
sqlmigrate 根据迁移文件内容输出相应的SQL语句
sqlsequencereset 重置数据表递增字段的索引值
squashmigrations 对迁移文件进行压缩处理
startapp 创建项目应用App
optimizemigration 允许优化迁移操作
startproject 创建新的Django项目
test 运行App里面的测试程序
testserver 新建测试数据库并使用该数据库运行项目
clearsessions 清除会话Session数据
collectstatic 收集所有的静态文件
findstatic 查找静态文件的路径信息
runserver 在本地计算机上启动Django项目


# 4 Application

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


我们来解释下这些生成的python文件。
- `__init__.py `：说明目录是一个python模块
- migrations.py目录：用于存放数据库迁移历史文件
- models.py : 用于应用操作数据库的模型
- views.py : 用于编写Web应用视图，接收数据，处理数据，与Model(模型) Template(模版)进行交互，返回应答
- apps.py ：应用配置文件。
- tests.py ：做单元测试。
- admin.py ：默认提供了admin后台管理，用作网站的后台管理站点配置相关



# 5 例子 创建HelloWorldProject

前面对应用创建和应用配置掌握后，我们来编写第一个Hello World应用吧。体验一把Django5的项目开发过程。



## 5.1 创建Hello World应用
直接执行startapp helloWorld 命令创建应用




## 5.2 注册应用到项目的settings.py

![](images/Pasted%20image%2020240618233454.png)


把helloWorld应用的apps.py里的HelloworldConfig类注册到settings.py里去
![](images/Pasted%20image%2020240618233506.png)

## 5.3 编写模版网页代码index.html

在templates目录下，新建index.html文件

![](images/Pasted%20image%2020240618233539.png)


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p>Django5大爷你好！</p>
<a href="http://python222.com/post/7" target="_blank">Python学习路线图</a>
</body>
</html>
```

## 5.4 编写视图处理请求层代码
在应用的views.py里编写index方法,request是客户端请求对象,render是渲染方法，可以携带数据渲染
到指定页面

```
def index(request):
return render(request,'index.html')
```



## 5.5 编写请求映射函数配置
在项目的urls.py里编写应用的index/请求，执行我们上面应用定义的请求处理代码，也就是写一个映射关系代码。


```
import helloWorld.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', helloWorld.views.index,
]
```


![](images/Pasted%20image%2020240618233805.png)


## 5.6 启动项目，测试

我们可以用前面讲的Django5的操作命令 runserver 启动

![](images/Pasted%20image%2020240618233833.png)

默认端口 8000
当然我们还有更简单的方式。直接用PyCharm启动。直接点击绿色小三角即可。

![](images/Pasted%20image%2020240618233841.png)



启动后，浏览器输入，因为我们项目urls.py里配置的请求地址就是index/ 所以请求如下

![](images/Pasted%20image%2020240618233912.png)

运行测试成功。
执行过程：客户端请求index/ - > 经过django url请求分发器 - > 执行到应用的views.py的index方法 - >
index方法再render渲染到index.html模版代码 - > 最终显示到用户浏览器终端。



