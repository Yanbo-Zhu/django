
> 其实就是函数, 对数据进行处理

在模版中，有时候需要对一些数据进行处理以后才能使用。一般在Python 中我们是通过函数的形式来完成的。
而在模版中，则是通过过滤器来实现的。过滤器使用的是| 来使用。比如使用add 过滤器，那么示例代码如下：
`{{ value|add:"2" }}`

把需要处理的变量写在前面, 把 函数写在后面 

Django过滤器是一种用于在Django模板中处理数据的技术。过滤器的作用是可以对模板中的变量进行加工、过滤或格式化，返回一个新的值供模板使用。

过滤器作用是在变量输出时，对输出的变量值做进一步的处理。
我们可以使用过滤器来更改变量的输出显示。
过滤器跟模板标签一样，也是在模板中对函数进行调用
对输出的日期进行格式化处理，或者转换大小写字母等，这些都有对应的过滤器去处理它们。

过滤器的语法格式如下：
	{{ 变量 | 过滤器1:参数值1 | 过滤器2:参数值2 ... }}

# 1 语法
## 1.1 常用内置过滤器

过滤器说明
add 加法
addslashes 添加斜杠
capfirst 首字母大写
center 文本居中
cut 切除字符
date 日期格式化
default 设置默认值
default_if_none 为None设置默认值
dictsort 字典排序
dictsortreversed 字典反向排序
divisibleby 整除判断
escape 转义
escapejs 转义js代码
filesizeformat 文件尺寸人性化显示
first 第一个元素
floatformat 浮点数格式化
force_escape 强制立刻转义
get_digit 获取数字
iriencode 转换IRI
join 字符列表链接
last 最后一个
length 长度
length_is 长度等于
linebreaks 行转换
linebreaksbr 行转换
linenumbers 行号
ljust 左对齐
lower 小写
make_list 分割成字符列表
phone2numeric 电话号码
过滤器说明
pluralize 复数形式
pprint 调试
random 随机获取
rjust 右对齐
safe 安全确认
safeseq 列表安全确认
slice 切片
slugify 转换成ASCII
stringformat 字符串格式化
striptags 去除HTML中的标签
time 时间格式化
timesince 从何时开始
timeuntil 到何时多久
title 所有单词首字母大写
truncatechars 截断字符
truncatechars_html 截断字符
truncatewords 截断单词
truncatewords_html 截断单词
unordered_list 无序列表
upper 大写
urlencode 转义url
urlize url转成可点击的链接
urlizetrunc urlize的截断方式
wordcount 单词计数
wordwrap 单词包裹
yesno 将True，False和None，映射成字符串‘yes’，‘no’，‘maybe’

## 1.2 根据给定的格式格式化日期

格式字
符
描述示例输出
a ‘a.m.’ or ‘p.m.’ ‘a.m.’
A ‘AM’ or ‘PM’ ‘AM’
b 月份，文字形式，3个字幕库，小写'jan'
B 未实现
c ISO 8601格式
2008-01-
02T10:30:00.000123+02:00
d 月的日子，带前导零的2位数字。01'到'31'
D 周几的文字表述形式，3个字母。'Fri'
e 时区名称"，'GMT,'-500'，US/Eastern'等
E 月份，分地区。
f 时间1'，1:30'
g 12小时格式，无前导零。"1'到'12'
G 24小时格式，无前导零。0'到'23'
h 12小时格式。'01'到'12'
H 24小时格式。'00'到23'
i 分钟00'到59'
I 夏令时间，无论是否生效。'1'或0
j 没有前导零的月份的日子。'1'到"31'
l 星期几,完整英文名'Friday'
L 布尔值是否是—个闰年。True或False
m 月，2位数字带前导零。'01'到'12'
M 月，文字，3个字母。"Jan”
n 月无前导零。'1'到'12'
N 美联社风格的月份缩写。'Jan.' ,'Feb.','March','May'
o ISO-8601周编号'1999'
O 与格林威治时间的差，单位小时。'+0200'
P 时间为12小时
1:30 p.m.’ , ‘midnight’ , ‘noon’ ,
‘12:30 p.m.’
r RFC 5322格式化日期。'Thu,21 Dec 2000 16:01:07+0200'
s 秒，带前导零的2位数字。'00'到59'
S 一个月的英文序数后缀，2个字符。'st' ,'nd', 'rd'或'th'
t 给定月份的天数。28 to 31
u 微秒。000000 to 999999
U
自Unix Epoch以来的秒数(1970年1月1日
00:00:00 UTC).
w 星期几,数字无前导零。'O'（星期日)至'6’(星期六)
W ISO-8601周数，周数从星期一开始。1，53
y 年份，2位数字。99
Y 年，4位数。'1999'
z —年中的日子0到365
Z 时区偏移量，单位为秒。-43200到43200

# 2 常用内置过滤器
## 2.1 add

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

## 2.2 Cut

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



## 2.3 date


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

![](03_模版_template/images/Pasted%20image%2020240616181933.png)


## 2.4 default

如果值被评估为False 。比如`[]` ， "" ， None ， {} 等这些在if 判断中为False 的值，都会使用 default 过滤器提供的默认值。示例代码如下：


```
{{ value|default:"nothing" }}
```

如果value 是等于一个空的字符串。比如"" ，那么以上代码将会输出nothing 。

## 2.5 default_if_none


如果值是None ，那么将会使用default_if_none 提供的默认值。这个和default 有区别， default 是所有被评估为False 的都会使用默认值。而default_if_none 则只有这个值是等于None 的时候才会使用默认值。示例代码如下：
``
{{ value|default_if_none:"nothing" }}

如果value 是等于"" 也即空字符串，那么以上会输出空字符串。如果value 是一个None 值，以上代码才会输出nothing 。

## 2.6 first
返回列表/元组/字符串中的第一个元素。示例代码如下：
`{{ value|first }}`

如果value 是等于`['a','b','c']` ，那么输出将会是a 。

## 2.7 last

返回列表/元组/字符串中的最后一个元素。示例代码如下：

`{{ value|last }}`

如果value 是等于`['a','b','c'] `，那么输出将会是c 。

## 2.8 floatformat

使用四舍五入的方式格式化一个浮点类型。如果这个过滤器没有传递任何参数。那么只会在小数点后保留一个小数，如果小数后面全是0，那么只会保留整数。当然也可以传递一个参数，标识具体要保留几个小数。

![](03_模版_template/images/Pasted%20image%2020240616182353.png)


## 2.9 join

类似与Python 中的join ，将列表/元组/字符串用指定的字符进行拼接。示例代码如下：

`{{ value|join:"/" }}`

如果value 是等于`['a','b','c'] `，那么以上代码将输出a/b/c 。


## 2.10 length

获取一个列表/元组/字符串/字典的长度。示例代码如下：

`{{ value|length }}`

如果value 是等于`['a','b','c'] `，那么以上代码将输出3 。如果value 为None ，那么以上将返回
0 。

## 2.11 lower

将值中所有的字符全部转换成小写。示例代码如下：
`{{ value|lower }}`

如果value 是等于Hello World 。那么以上代码将输出hello world 。

## 2.12 upper


类似于lower ，只不过是将指定的字符串全部转换成大写。

## 2.13 random 

在被给的列表/字符串/元组中随机的选择一个值。示例代码如下：

`{{ value|random }}`

如果value 是等于`['a','b','c'] `，那么以上代码会在列表中随机选择一个。

## 2.14 safe

标记一个字符串是安全的。也即会关掉这个字符串的自动转义。示例代码如下：

`{{value|safe}}`

如果value 是一个不包含任何特殊字符的字符串，比如`<a> `这种，那么以上代码就会把字符串正常的输
入。如果value 是一串html 代码，那么以上代码将会把这个html 代码渲染到浏览器中

## 2.15 slice 

类似于Python 中的切片操作。示例代码如下：
`{{ some_list|slice:"2:" }}`

以上代码将会给some_list 从2 开始做切片操作。


## 2.16 stringtags

删除字符串中所有的html 标签。示例代码如下：

{{ value|striptags }}

如果value 是<strong>hello world</strong> ，那么以上代码将会输出hello world 。



## 2.17 truncatechars

如果给定的字符串长度超过了过滤器指定的长度。那么就会进行切割，并且会拼接三个点来作为省略
号。示例代码如下：

```
{{ value|truncatechars:5 }}
```

如果value 是等于北京欢迎您~ ，那么输出的结果是北京... 。可能你会想，为什么不会北京欢迎您...
呢。因为三个点也占了三个字符，所以北京+ 三个点的字符长度为5


## 2.18 truncatechars_html

类似于truncatechars ，只不过是不会切割html 标签。示例代码如下：

`{{ value|truncatechars:5 }}`

`如果value 是等于<p>北京欢迎您~</p> ，那么输出将是<p>北京...</p> 。`


# 3 例子 1



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


# 4 例子 2

views.py index函数我们修改下：str改成"hello"，再定义一个日期对象

```
def index(request):
	str = "hello"
	date = datetime.datetime.now()
	myDict = {"tom": '666', 'cat': '999', 'wzw': '333'}
	# 创建一个对象 zhangsan
	zhangsan = Person("张三", 21)
	myList = ["java", "python", "c"]
	myTuple = ("python", 222, 3.14, False)
	content_value = {"msg": str, "msg2": myDict, "msg3": zhangsan, "msg4":
	myList, "msg5": myTuple, "date": date}
	return render(request, 'index.html', context=content_value)
```

index.html加下：
```
<p>内置过滤器</p>
capfirst:{{ msg | capfirst }}<br>
length:{{ msg | length }}<br>
date:{{ date }} - >> {{ date | date:'Y-m-d H:i:s' }}
```

运行测试：
![[03_模版_template/images/Pasted image 20240619172740.png]]




