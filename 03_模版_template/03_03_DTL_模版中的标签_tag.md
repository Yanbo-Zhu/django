
https://docs.djangoproject.com/en/5.0/ref/templates/builtins/

标签是对模板上下文进行控制输出，它是以{% tag %}表示的，其中 tag是标签的名称，Django内置了许
多模板标签，比如{% if %}（判断标签）、{% for %}(循环标签）或{% url %}(路由标签）等。
常用内置标签如下：

标签描述
{% for %} 遍历输出上下文的内容
{% if %} 对上下文进行条件判断
{% csrf_token %} 生成csrf token的标签，用于防护跨站请求伪造攻击
{% url %} 引用路由配置的地址，生成相应的路由地址
{% with %} 将上下文名重新命名
{% load %} 加载导入 Django的标签库
{% static %} 读取静态资源的文件内容
{% extends xxx %} 模板继承，xxx为模板文件名，使当前模板继承xxx模板
{% block xxx %} 重写父类模板的代码

# 1 if 标签： 

if 标签相当于Python 中的if 语句，有elif 和else 相对应，但是所有的标签都需要
用标签符号（ `{%%} `）进行包裹。if 标签中可以使用`==、!=、<、<=、>、>=、in、not in、is、is not `等判断运算符。示例代码如下：

```
{% if "张三" in persons %}
    <p>张三</p>
{% else %}
    <p>李四</p>
{% endif %}
```


# 2 for...in... 标签：

for...in... 类似于Python 中的for...in... 。可以遍历列表、元组、字
符串、字典等一切可以遍历的对象。示例代码如下：

```
{% for person in persons %}
    <p>{{ person.name }}</p>
{% endfor %}
```

如果想要反向遍历，那么在遍历的时候就加上一个reversed 。示例代码如下：


```
{% for person in persons reversed %}
    <p>{{ person.name }}</p>
{% endfor %}
```

遍历字典的时候，需要使用items 、keys 和values 等方法。在DTL 中，执行一个方法不能使用圆括号的形式。遍历字典示例代码如下：


```
{% for key,value in person.items %}
    <p>key：{{ key }}</p>
    <p>value：{{ value }}</p>
{% endfor %}
```


在for 循环中， DTL 提供了一些变量可供使用。这些变量如下：
- forloop.counter ：当前循环的下标。以1作为起始值。
- forloop.counter0 ：当前循环的下标。以0作为起始值。
- forloop.revcounter ：当前循环的反向下标值。比如列表有5个元素，那么第一次遍历这个属性是等于5，第二次是4，以此类推。并且是以1作为最后一个元素的下标。
- forloop.revcounter0 ：类似于forloop.revcounter 。不同的是最后一个元素的下标是从0开始。
- forloop.first ：是否是第一次遍历。
- forloop.last ：是否是最后一次遍历。
- forloop.parentloop ：如果有多个循环嵌套，那么这个属性代表的是上一级的for循环。


# 3 for...in...empty 标签：

这个标签使用跟for...in... 是一样的，只不过是在遍历的对象如果没有元素的情况下，会执行empty 中的内容。示例代码如下：

```
{% for person in persons %}
    <li>{{ person }}</li>
{% empty %}
    暂时还没有任何人
{% endfor %}
```


# 4 with 标签

在模版中定义变量。有时候一个变量访问的时候比较复杂，那么可以先把这个复杂的变量缓存到一个变量上，以后就可以直接使用这个变量就可以了。示例代码如下：

```
context = {
    "persons": ["张三","李四"]
}

{% with lisi=persons.1 %}
    <p>{{ lisi }}</p>
{% endwith %}
```



有几点需要强烈的注意：
- 在with 语句中定义的变量，只能在{%with%}{%endwith%} 中使用，不能在这个标签外面使用。
- 定义变量的时候，不能在等号左右两边留有空格。比如{% with lisi = persons.1%} 是错误的。
- 还有另外一种写法同样也是支持的：

```
{% with persons.1 as lisi %}
    <p>{{ lisi }}</p>
{% endwith %}
```



# 5 url 标签

在模版中，我们经常要写一些url ，比如某个a 标签中需要定义href 属性。当然如果
通过硬编码的方式直接将这个url 写死在里面也是可以的。但是这样对于以后项目维护可能不是一件好事。
因此建议使用这种反转的方式来实现，类似于django 中的reverse 一样。

示例代码如下：

```
<a href="{% url 'book:list' %}">图书列表页面</a>
```

如果url 反转的时候需要传递参数，那么可以在后面传递。但是参数分位置参数和关键字参数。位置参数和关键字参数不能同时使用。

示例代码如下
```
# path部分
path('detail/<book_id>/',views.book_detail,name='detail')

# url反转，使用位置参数
<a href="{% url 'book:detail' 1 %}">图书详情页面</a>

# url反转，使用关键字参数
<a href="{% url 'book:detail' book_id=1 %}">图书详情页面</a>
```

如果想要在使用url 标签反转的时候要传递查询字符串的参数，那么必须要手动在在后面添加。示例代码如下：
`<a href="{% url 'book:detail' book_id=1 %}?page=1">图书详情页面</a>`

如果需要传递多个参数，那么通过空格的方式进行分隔。示例代码如下：
`<a href="{% url 'book:detail' book_id=1 page=2 %}">图书详情页面</a>`

# 6 spaceless 标签

移除html标签中的空白字符。包括空格、tab键、换行等。示例代码如下

```
{% spaceless %}
    <p>
        <a href="foo/">Foo</a>
    </p>
{% endspaceless %}
```

那么在渲染完成后，会变成以下的代码：

```
<p><a href="foo/">Foo</a></p>
```

spaceless 只会移除html标签之间的空白字符。而不会移除标签与文本之间的空白字符。看以下代码：

```
{% spaceless %}
    <strong>
        Hello
    </strong>
{% endspaceless %}
```

这个将不会移除strong 中的空白字符。

# 7 autoescape 标签：


开启和关闭这个标签内元素的自动转义功能。自动转义是可以将一些特殊的字
符。比如< 转义成html 语法能识别的字符，会被转义成< ，而> 会被自动转义成> 。模板中默认是已经开启了自动转义的。
autoescape 的示例代码如下
```
# 传递的上下文信息
context = {
    "info":"<a href='www.baidu.com'>百度</a>"
}
# 模板中关闭自动转义
{% autoescape off %}
    {{ info }}
{% endautoescape %}
```


那么就会显示百度的一个超链接。如果把off 改成on ，那么就会显示成一个普通的字符串。示例 代码如下：
```
{% autoescape on %}
    {{ info }}
{% endautoescape %}
```


# 8 verbatim 标签：

默认在DTL 模板中是会去解析那些特殊字符的。比如{% 和%} 以及{{ 等。如果你
在某个代码片段中不想使用DTL 的解析引擎。那么你可以把这个代码片段放在verbatim 标签中。

示例代码下：
```
{% verbatim %}
    {{if dying}}Still alive.{{/if}}
{% endverbatim %}
```


# 9 特殊的变量来获取for标签的循环信息

在for标签中，模板还提供了一些特殊的变量来获取for标签的循环信息，变量说明如下：

变量描述
forloop.counter 获取当前循环的索引，从1开始计算
forloop.counter0 获取当前循环的索引，从0开始计算
forloop.revcounter 索引从最大数开始递减，直到索引到1位置
forloop.revcounter0 索引从最大数开始递减，直到索引到0位置
forloop.first 当遍历的元素为第一项时为真
forloop.last 当遍历的元素为最后一项时为真
forloop.parentloop 在嵌套的for循环中，获取上层for循环的forloop


我们修改index.html：

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
        <h3>模板标签</h3>
        <p>遍历for标签：</p>
        {% for item in msg4 %}
        <p>这个是第{{ forloop.counter }}次循环</p>
        {% if forloop.first %}
        <p>这个是第一项：{{ item }}</p>
        {% elif forloop.last %}
        <p>这个是最后一项：{{ item }}</p>
        {% endif %} {% endfor %}
        <p>判断if标签：</p>
        {% if msg == '模板变量' %}
        <p>模板变量</p>
        {% elif msg == '模板变量2' %}
        <p>模板变量2</p>
        {% else %}
        <p>其他</p>
        {% endif %}
        <p>url标签</p>
        <a href="{% url 'index' %}">请求index</a>
        <p>with标签</p>
        {% with info=msg %} {{ info }} {% endwith %}
    </body>
</html>

```


用url标签的时候 第二个参数是路由名称，所以urls.py里，修改下：
`path('index/', helloWorld.views.index, name="index"),`


测试，浏览器输入： http://127.0.0.1:8000/index/
![[03_模版_template/images/Pasted image 20240619171319.png]]

