
> 其实就是函数, 对数据进行处理

在模版中，有时候需要对一些数据进行处理以后才能使用。一般在Python 中我们是通过函数的形式来完成的。
而在模版中，则是通过过滤器来实现的。过滤器使用的是| 来使用。比如使用add 过滤器，那么示例代码如下：
`{{ value|add:"2" }}`

把需要处理的变量写在前面, 把 函数写在后面 


# 1 add

将传进来的参数添加到原来的值上面。这个过滤器会尝试将值和参数转换成整形然后进行相加。如果转换成整形过程中失败了，那么会将值和参数进行拼接。如果是字符串，那么会拼接成字符串，如果是列表，那么会拼接成一个列表。示例代码如下：

```
{{ value|add:"2" }}
```


如果value 是等于4，那么结果将是6。如果value 是等于一个普通的字符串，比如abc ，那么结果将是abc2 。add 过滤器的源代码如下：

```
def add(value, arg):
    """Add the arg to the value."""
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''
```

# 2 Cut

移除值中所有指定的字符串。类似于python 中的replace(args,"") 。示例代码如下：

`{{ value|cut:" " }}`

以上示例将会移除value 中所有的空格字符。cut 过滤器的源代码如下：

```
def cut(value, arg):
    """Remove all values of arg from the given string."""
    safe = isinstance(value, SafeData)
    value = value.replace(arg, '')
    if safe and arg != ';':
        return mark_safe(value)
    return value
```



# 3 date


将一个日期按照指定的格式，格式化成字符串。示例代码如下：

```
# 数据
context = {
    "birthday": datetime.now()
}

# 模版
{{ birthday|date:"Y/m/d" }}
```


那么将会输出2058/02/01 。其中Y 代表的是四位数字的年份， m 代表的是两位数字的月份， d 代表的是两位数字的日。

![](images/Pasted%20image%2020240616181933.png)


# 4 default

如果值被评估为False 。比如`[]` ， "" ， None ， {} 等这些在if 判断中为False 的值，都会使用 default 过滤器提供的默认值。示例代码如下：


```
{{ value|default:"nothing" }}
```

如果value 是等于一个空的字符串。比如"" ，那么以上代码将会输出nothing 。

# 5 default_if_none


如果值是None ，那么将会使用default_if_none 提供的默认值。这个和default 有区别， default 是所有被评估为False 的都会使用默认值。而default_if_none 则只有这个值是等于None 的时候才会使用默认值。示例代码如下：
``
{{ value|default_if_none:"nothing" }}

如果value 是等于"" 也即空字符串，那么以上会输出空字符串。如果value 是一个None 值，以上代码才会输出nothing 。

# 6 first
返回列表/元组/字符串中的第一个元素。示例代码如下：
`{{ value|first }}`

如果value 是等于`['a','b','c']` ，那么输出将会是a 。

# 7 last

返回列表/元组/字符串中的最后一个元素。示例代码如下：

`{{ value|last }}`

如果value 是等于`['a','b','c'] `，那么输出将会是c 。

# 8 floatformat

使用四舍五入的方式格式化一个浮点类型。如果这个过滤器没有传递任何参数。那么只会在小数点后保留一个小数，如果小数后面全是0，那么只会保留整数。当然也可以传递一个参数，标识具体要保留几个小数。

![](images/Pasted%20image%2020240616182353.png)


# 9 join

类似与Python 中的join ，将列表/元组/字符串用指定的字符进行拼接。示例代码如下：

`{{ value|join:"/" }}`

如果value 是等于`['a','b','c'] `，那么以上代码将输出a/b/c 。


# 10 length

获取一个列表/元组/字符串/字典的长度。示例代码如下：

`{{ value|length }}`

如果value 是等于`['a','b','c'] `，那么以上代码将输出3 。如果value 为None ，那么以上将返回
0 。

# 11 lower

将值中所有的字符全部转换成小写。示例代码如下：
`{{ value|lower }}`

如果value 是等于Hello World 。那么以上代码将输出hello world 。

# 12 upper


类似于lower ，只不过是将指定的字符串全部转换成大写。

# 13 random 

在被给的列表/字符串/元组中随机的选择一个值。示例代码如下：

`{{ value|random }}`

如果value 是等于`['a','b','c'] `，那么以上代码会在列表中随机选择一个。

# 14 safe

标记一个字符串是安全的。也即会关掉这个字符串的自动转义。示例代码如下：

`{{value|safe}}`

如果value 是一个不包含任何特殊字符的字符串，比如`<a> `这种，那么以上代码就会把字符串正常的输
入。如果value 是一串html 代码，那么以上代码将会把这个html 代码渲染到浏览器中

# 15 slice 

类似于Python 中的切片操作。示例代码如下：
`{{ some_list|slice:"2:" }}`

以上代码将会给some_list 从2 开始做切片操作。


# 16 stringtags

删除字符串中所有的html 标签。示例代码如下：

{{ value|striptags }}

如果value 是<strong>hello world</strong> ，那么以上代码将会输出hello world 。



# 17 truncatechars

如果给定的字符串长度超过了过滤器指定的长度。那么就会进行切割，并且会拼接三个点来作为省略
号。示例代码如下：

```
{{ value|truncatechars:5 }}
```

如果value 是等于北京欢迎您~ ，那么输出的结果是北京... 。可能你会想，为什么不会北京欢迎您...
呢。因为三个点也占了三个字符，所以北京+ 三个点的字符长度为5


# 18 truncatechars_html

类似于truncatechars ，只不过是不会切割html 标签。示例代码如下：

`{{ value|truncatechars:5 }}`

`如果value 是等于<p>北京欢迎您~</p> ，那么输出将是<p>北京...</p> 。`


# 19 例子



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
    path('filter', views.filter_view, name='filter'), ## 这里 
    path('template/form', views.template_form, name='template_form'),
    path('sta', views.static_view, name='static_view')
]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```



views.py 
```python 
def filter_view(request):
    greet = "Hello World, Hello Django"
    context = {
        "greet": greet,
        'birthday': datetime.now(),
        'profile': "xxx",
        'html': "<h1>欢迎来到知了课堂！</h1>"
    }
    return render(request, "filter.html", context=context)
```


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>过滤器的使用</title>
</head>
<body>
<p>{{ greet|cut:"," }}</p>
<p>生日：{{ birthday|date:"Y年m月d日" }}</p>
<p>个人简介：{{ profile|default:"这个家伙很懒，什么都没留下！" }}</p>
<div>{{ html|safe }}</div>
</body>
</html>
```
