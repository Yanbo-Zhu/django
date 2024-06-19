
# 1 HttpResponse对象

Django服务器接收到客户端发送过来的请求后，会将提交上来的这些数据封装成一个HttpRequest 对象传给视图函数。那么视图函数在处理完相关的逻辑后，也需要返回一个响应给浏览器。而这个响应，我们必须返回HttpResponseBase 或者他的子类的对象。而HttpResponse 则是HttpResponseBase 用得最多的子类。\

那么接下来就来介绍一下HttpResponse 及其子类

## 1.1 常用属性：
1. content：返回的内容。
2. status_code：返回的HTTP响应状态码。
3. content_type：返回的数据的MIME类型，默认为text/html 。浏览器会根据这个属性，来显示数据。如果是text/html ，那么就会解析这个字符串，如果text/plain ，那么就会显示一个纯文本。常用的Content-Type 如下：
    1. text/html（默认的，html文件）
    2. text/plain（纯文本）
    3. text/css（css文件）
    4. text/javascript（js文件）
    5. multipart/form-data（文件提交）
    6. application/json（json传输）
    7. application/xml（xml文件）
4. 设置请求头： response['X-Access-Token'] = 'xxxx' 。


## 1.2 常用方法：
1. set_cookie：用来设置cookie 信息。后面讲到授权的时候会着重讲到。
2. delete_cookie：用来删除cookie 信息。
3. write： HttpResponse 是一个类似于文件的对象，可以用来写入数据到数据体（content）中。


## 1.3 JsonResponse类：

用来对象 dump 成json 字符串，然后返回将json 字符串封装成Response 对象返回给浏览器。并且他的Content-Type 是application/json 。示例代码如下
```
from django.http import JsonResponse

def index(request):
    return JsonResponse({"username":"zhiliao","age":18})
```


默认情况下JsonResponse 只能对字典进行dump ，如果想要对非字典的数据进行dump ，那么需要给JsonResponse 传递一个safe=False 参数
```
from django.http import JsonResponse

def index(request):
    persons = ['张三','李四','王五']
    return HttpResponse(persons)
```

以上代码会报错，应该在使用HttpResponse 的时候，传入一个safe=False 参数，示例代码如下：
`return HttpResponse(persons,safe=False)`


# 2 生成CSV文件

有时候我们做的网站，需要将一些数据，生成有一个CSV 文件给浏览器，并且是作为附件的形式下载下来。以下将讲解如何生成CSV 文件。

> 使用HttpResponse 来将csv 文件返回回去


## 2.1 生成小的CSV文件

这里将用一个生成小的CSV 文件为例，来把生成CSV 文件的技术要点讲到位。我们用Python 内置的csv 模块来处理csv 文件，并且使用HttpResponse 来将csv 文件返回回去。

```
import csv
from django.http import HttpResponse

def csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['username', 'age', 'height', 'weight'])
    writer.writerow(['zhiliao', '18', '180', '110'])
    
    return response
```

这里再来对每个部分的代码进行解释：
1. 我们在初始化HttpResponse 的时候，指定了Content-Type 为text/csv ，这将告诉浏览器，这是一个csv 格式的文件而不是一个HTML 格式的文件，如果用默认值，默认值就是html ，那么浏览器将把csv 格式的文件按照html 格式输出，这肯定不是我们想要的。
2. 第二个我们还在response 中添加一个Content-Disposition 头，这个东西是用来告诉浏览器该如何处理这个文件，我们给这个头的值设置为attachment; ，那么浏览器将不会对这个文件进行显示，而是作为附件的形式下载，第二个filename="somefilename.csv" 是用来指定这个csv 文件的名字。
3. 我们使用csv 模块的writer 方法，将相应的数据写入到response 中。


## 2.2 将csv文件定义成模板

我们还可以将csv 格式的文件定义成模板，然后使用Django 内置的模板系统，并给这个模板传入一个Context 对象，这样模板系统就会根据传入的Context 对象，生成具体的csv 文件。

模版文件
```python
{% for row in data %}"{{ row.0|addslashes }}", "{{ row.1|addslashes }}", "{{row.2|addslashes }}", "{{ row.3|addslashes }}", "{{ row.4|addslashes }}"
{% endfor %}
```


视图函数 
```
from django.http import HttpResponse
from django.template import loader, Context

def some_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    
    csv_data = (
        ('First row', 'Foo', 'Bar', 'Baz'),
        ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
    )
    
    t = loader.get_template('my_template_name.txt')
    response.write(t.render({"data": csv_data}))
    
    return response
```



## 2.3 生成大的CSV文件

以上的例子是生成的一个小的csv 文件，如果想要生成大型的csv 文件，那么以上方式将有可能会发生超时的情况（服务器要生成一个大型csv文件，需要的时间可能会超过浏览器默认的超时时间）。这时候我们可以借助另外一个类，叫做StreamingHttpResponse 对象，这个对象是将响应的数据作为一个流返回给客户端，而不是作为一个整体返回。


```python
class Echo:
"""
定义一个可以执行写操作的类，以后调用csv.writer的时候，就会执行这个方法
"""
    def write(self, value):
        return value
        
def large_csv(request):
    rows = (["Row {}".format(idx), str(idx)] for idx in range(655360))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)

    response = StreamingHttpResponse((writer.writerow(row) for row in
rows),content_type="text/csv")

    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    
    return response
```


这里我们构建了一个非常大的数据集rows ，并且将其变成一个迭代器。然后因为 StreamingHttpResponse 的第一个参数只能是一个生成器，因此我们使用圆括号 (writer.writerow(row) for row in rows) ，并且因为我们要写的文件是csv 格式的文件，因此需
要调用writer.writerow将row变成一个csv 格式的字符串。

而调用writer.writerow又需要一个中间的容器，因此这里我们定义了一个非常简单的类Echo ，这个类只实现一个write 方法，以后在执行 csv.writer(pseudo_buffer) 的时候，就会调用Echo.writer 方法。

注意： StreamingHttpResponse 会启动一个进程来和客户端保持长连接，所以会很消耗资源。所以如果不是特殊要求，尽量少用这种方法

## 2.4 关于StreamingHttpResponse

这个类是专门用来处理流数据的。使得在处理一些大型文件的时候，不会因为服务器处理时间过长而到时连接超时。这个类不是继承自HttpResponse ，并且跟HttpResponse 对比有以下几点区别：
1. 这个类没有属性content ，相反是streaming_content 。
2. 这个类的streaming_content 必须是一个可以迭代的对象。
3. 这个类没有write 方法，如果给这个类的对象写入数据将会报错。
注意： StreamingHttpResponse 会启动一个进程来和客户端保持长连接，所以会很消耗资源。所以如果不是特殊要求，尽量少用这种方法


