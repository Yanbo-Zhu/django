
模板上下文是模板中基本的组成单位，上下文的数据由视图函数或视图类传递。它以{{ variable }}表示，variable是上下文的名称，它支持 Python 所有的数据类型，如字典、列表、元组、字符串、整型或实例化对象等。上下文的数据格式不同，在模板里的使用方式也有所差异。



模板中可以包含变量， Django 在渲染模板的时候，可以传递变量对应的值过去进行替换。
变量的命名规范和Python 非常类似，只能是阿拉伯数字和英文字符以及下划线的组合，不能出现标点符号等特殊字符。
变量需要通过视图函数渲染，视图函数在使用render 或者render_to_string 的时候可以传递一个 context 的参数，这个参数是一个字典类型。以后在模板中的变量就从这个字典中读取值的。

示例代码 如下：

```
# profile.html模板代码
<p>{{ username }}</p>

# views.py代码
def profile(request):
    return render(request,'profile.html',context={'username':'知了课堂'})
```

# 1 注意点 

使用变量的一些注意点如下：

- 当模板引擎遇到一个变量，将计算这个变量，然后输出结果
- 变量名必须由字母、数字、下划线、点组成，不能由数字和下划线开头
- 当模板引擎遇到 “ . ” 的时候，按以下顺序进行解析
	- 按照 dict 解析 var[key]
	- 按照对象的属性或方法解析 var.var/func
	- 按照索引解析 var[index]
- 如果变量不存在，不会引发异常，模板会插入空字符串 ''
- 在模板中使用变量或方法时，不能出现 ()、[]、{}
- 调用方法时，不能传递参数


有以下几点需要注意：
- html 文件中 不能通过中括号的形式访问字典和列表中的值，比如dict['key']和list[1]是不支持的！
- 因为使用点（.）语法获取对象值的时候，可以获取这个对象的属性，如果这个对象是一个字典，也可以获取这个字典的值。所以在给这个字典添加key的时候，千万不能和字典中的一些属性重复。比如items，因为items是字典的方法，那么如果给这个字典添加一个items作为key，那么以后就不能再通过item来访问这个字典的键值对了。

模板中的变量同样也支持点(.) 的形式。在出现了点的情况，比如person.username ，模板是按照以下 方式进行解析的：
1. 如果person 是一个字典，那么就会查找这个字典的username 这个key 对应的值。
2. 如果person 是一个对象，那么就会查找这个对象的username 属性，或者是username 这个方法。
3. 如果出现的是`person.1` ，会判断persons 是否是一个列表或者元组或者任意的可以通过下标访问的对象，如果是的话就取这个列表的第1个值。如果不是就获取到的是一个空的字符串。




# 2 例子


info.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>信息</title>
</head>
<body>
<p>{{ username }}</p>
<p>图书名称：{{ book.name }}</p>
<p>下标为1图书的名称：{{ books.1.name }}</p>
<p>姓名为：{{ person.realname }}</p>
</body>
</html>

```

urls.py
```python
from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('baidu', views.baidu, name='baidu'),
    path('info', views.info, name='info'),
    path('if', views.if_view, name='if'),
    path('for', views.for_view, name='for'),
    path('with', views.with_view, name='with'),
    path('url', views.url_view, name='url'),
    path('book/<book_id>', views.book_detail, name='book_detail'),
    path('filter', views.filter_view, name='filter'),
    path('template/form', views.template_form, name='template_form'),
    path('sta', views.static_view, name='static_view')
]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```


home/views.py
```python 
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
```



# 3 例子2

views.py，index方法：
```python
# 定义人类  
class Person:  
    # 属性 姓名  
    name = None  
    # 属性 年龄  
    age = None  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
  
def index(request):  
    str = "模板变量"  
    myDict = {"tom": '666', 'cat': '999', 'wzw': '333'}  
    # 创建一个对象 zhangsan    zhangsan = Person("张三", 21)  
    myList = ["java", "python", "c"]  
    myTuple = ("python", 222, 3.14, False)  
    content_value = {"msg": str, "msg2": myDict, "msg3": zhangsan, "msg4":  myList, "msg5": myTuple}  
    return render(request, 'index.html', context=content_value)
```

index.html:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Title</title>
    </head>
    <body>
        字符串：{{ msg }}<br />
        字典类型：{{ msg2.tom }},{{ msg2.cat }},{{ msg2.wzw }}<br />
        对象：{{ msg3.name }},{{ msg3.age }}<br />
        列表：{{ msg4.0 }},{{ msg4.1 }},{{ msg4.3 }},{{ msg4.2 }}<br />
        元组：{{ msg5.0 }},{{ msg5.4 }},{{ msg5.1 }},{{ msg5.2 }},{{ msg5.3 }}
    </body>
</html>

```


测试，浏览器输入： http://127.0.0.1:8000/index/
![[03_模版/images/Pasted image 20240619170742.png]]

