
![](images/Pasted%20image%2020240615171403.png)


输入 url, 根据path 知道要呼叫那个视图函数, 通过这个函数 调取 数据库 中的某个 信息. 然后回传给user 

![](images/Pasted%20image%2020240615171653.png)

# 1 视图 views.py

视图一般都写在app 的views.py 中。并且视图的第一个参数永远都是request （一个 HttpRequest）对象。这个对象存储了请求过来的所有信息，包括携带的参数以及一些头部信息等。在视图中，一般是完成逻辑相关的操作。
比如这个请求是添加一篇博客，那么可以通过request来接收到这些数据，然后存储到数据库中，最后再把执行的结果返回给浏览器。视图函数的返回结果必须是 HttpResponseBase 对象或者子类的对象。

示例代码如下：

```
from django.http import HttpResponse
def book_list(request):
return HttpResponse("书籍列表！")
```


视图可以是函数，也可以是类，我们先学习函数视图，后面再学习类视图。

