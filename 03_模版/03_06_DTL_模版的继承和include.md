

# 1 include模版 

有时候一些代码是在许多模版中都用到的。如果我们每次都重复的去拷贝代码那肯定不符合项目的规范。一般我们可以把这些重复性的代码抽取出来，就类似于Python中的函数一样，以后想要使用这些代码的时候，就通过include 包含进来。这个标签就是include 。示例代码如下：


```
# header.html
<p>我是header</p>
# footer.html
<p>我是footer</p>


# main.html
{% include 'header.html' %}
<p>我是main内容</p>
{% include 'footer.html' %}
```


include 标签寻找路径的方式。也是跟render 渲染模板的函数是一样的。

默认include 标签包含模版，会自动的使用主模版中的上下文，也即可以自动的使用主模版中的变量。如果想传入一些其他的参数，那么可以使用with 语句。

示例代码如下：
```
# header.html
<p>用户名：{{ username }}</p>

# main.html
{% include "header.html" with username='huangyong' %}
```


# 2 模版继承


在前端页面开发中。有些代码是需要重复使用的。这种情况可以使用include 标签来实现。也可以使用另外一个比较强大的方式来实现，那就是模版继承。

模版继承类似于Python 中的类，在父类中可以先定义好一些变量和方法，然后在子类中实现。模版继承也可以在父模版中先定义好一些子模版需要用到的代码，然后子模版直接继承就可以了。并且因为子模版肯定有自己的不同代码，因此可以在父模版中定义一个block接口，然后子模版再去实现。

Django模板继承是一个强大的工具，可以将通用页面元素（例如页眉、页脚、侧边栏等）分离出来，并在多个页面之间共享他们。

模板继承和 Python 语言中类的继承含义是一样的，在 Django 中模板只是一个文本文件，如 HTML。

模板继承是 Django 模板语言中最强大的部分。模板继承使你可以构建基本的“骨架”模板，将通用的功能或者属性写在基础模板中，也叫基类模板或者父模板。子模板可以继承父类模板，子模板继承后将自动拥有父类中的属性和方法，我们还可以在子模板中对父模板进行重写，即重写父模板中方法或者属性，从而实现子模板的定制。模板继承大大提高了代码的可重用性，减轻开发人员的工作量。

> 在模板继承中最常用了标签就是 {% block %} 与 {% extends %} 标签，其中 {% block% } 标签与 {%
endblock %} 标签成对出现


需要注意的是：
- extends标签必须放在模版的第一行。子模板中的代码必须放在block中，否则将不会被渲染。
- 如果在某个block 中需要使用父模版的内容，那么可以使用{{block.super}} 来继承。比如上例， {%block title%} ，如果想要使用父模版的title ，那么可以在子模版的title block 中使用{{ block.super }} 来实现。
- 在定义block 的时候，除了在block 开始的地方定义这个block 的名字，还可以在block 结束的时候定义名字。比如{% block title %}{% endblock title %}. 这在待选哪个末班中显得尤为有用, 能让你快速的看到block包含在哪里 


## 2.1 例子1

以下是父模版的代码：

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{% static 'style.css' %}" />
    <title>{% block title %}我的站点{% endblock %}</title>
</head>

<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">首页</a></li>
            <li><a href="/blog/">博客</a></li>
        </ul>
        {% endblock %}
    </div>
    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```


这个模版，我们取名叫做base.html ，定义好一个简单的html 骨架，然后定义好两个block 接口，让子模版来根据具体需求来实现。子模板然后通过extends 标签来实现，示例代码如下：

```
{% extends "base.html" %}

{% block title %}博客列表{% endblock %}

{% block content %}
    {% for entry in blog_entries %}
        <h2>{{ entry.title }}</h2>
        <p>{{ entry.body }}</p>
    {% endfor %}
{% endblock %}
```


## 2.2 例子2 

我们新建一个基础模版base.html
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>
            {% block title %} Python222学院 {% endblock %}
        </title>
    </head>
    <body>
        <div id="head">
            <img src="http://127.0.0.1:8000/static/logo.png" />
        </div>
        <div id="content">
            {% block content %} 欢迎进入Python222学院 {% endblock %}
        </div>
        <div id="footer">
            版权所有 www.python222.com
        </div>
    </body>
</html>

```

再写一个course.html，继承base.html
```html
{% extends 'base.html' %}
<!-- 重写title -->
{% block title %}
课程页面-Python222
{% endblock %}
<!-- 重写content -->
{% block content %}
Django5课程-模板引擎章节
{% endblock %}
```

我们来测试下吧。
views.py里新建一个to_course方法：

```
def to_course(request):
	"""
	跳转课程页面
	:param request:
	:return:
	"""
	return render(request, 'course.html')
```

urls.py里加一个映射：
`path('toCourse/', helloWorld.views.to_course)`


浏览器输入： http://127.0.0.1:8000/toCourse/
![[03_模版/images/Pasted image 20240619172228.png]]

我们发现模板里的标题和内容被course页面修改了，其他的没变。

这里我们再优化下，直接写死静态路径是不是很不好啊。
```html
<div id="head">
	<img src="http://127.0.0.1:8000/static/logo.png"/>
</div>
```

这时候我们就能用上 {% load static %} ，加载项目中的静态文件，包括图片，css，js文件，字体文
件等。
```
<img src="{% static 'logo.png' %}"/>
```

完整base.html：
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>
            {% block title %} Python222学院 {% endblock %}
        </title>
    </head>
    {% load static %}
    <body>
        <div id="head">
            <img src="{% static 'logo.png' %}" />
        </div>
        <div id="content">
            {% block content %} 欢迎进入Python222学院 {% endblock %}
        </div>
        <div id="footer">
            版权所有 www.python222.com
        </div>
    </body>
</html>

```


