
# 1 WSGIRequest对象常用属性和方法

Django在接收到http请求之后，会根据http请求携带的参数以及报文信息创建一个WSGIRequest 对象，并且作为视图函数第一个参数传给视图函数。也就是我们经常看到的request 参数。在这个对象上我们可以找到客户端上传上来的所有信息。这个对象的完整路径是
django.core.handlers.wsgi.WSGIRequest 。

对象常用属性：
WSGIRequest 对象上大部分的属性都是只读的。因为这些属性是从客户端上传上来的，没必要做任何的修改。

以下将对一些常用的属性进行讲解：
1. path ：请求服务器的完整“路径”，但不包含域名和参数。比如
http://www.baidu.com/xxx/yyy/ ，那么path 就是/xxx/yyy/ 。
2. method ：代表当前请求的http 方法。比如是GET 还是POST 。
3. GET ：一个django.http.request.QueryDict 对象。操作起来类似于字典。这个属性中包含了所
有以?xxx=xxx 的方式上传上来的参数。
4. POST ：也是一个django.http.request.QueryDict 对象。这个属性中包含了所有以POST 方式上
传上来的参数。
5. FILES ：也是一个django.http.request.QueryDict 对象。这个属性中包含了所有上传的文件。
6. COOKIES ：一个标准的Python字典，包含所有的cookie ，键值对都是字符串类型。
7. session ：一个类似于字典的对象。用来操作服务器的session 。
8. META ：存储的客户端发送上来的所有header 信息。
9. CONTENT_LENGTH ：请求的正文的长度（是一个字符串）。
10. CONTENT_TYPE ：请求的正文的MIME类型。
11. HTTP_ACCEPT ：响应可接收的Content-Type。
12. HTTP_ACCEPT_ENCODING ：响应可接收的编码。
13. HTTP_ACCEPT_LANGUAGE ： 响应可接收的语言。
14. HTTP_HOST ：客户端发送的HOST值。
15. HTTP_REFERER ：在访问这个页面上一个页面的url。
16. QUERY_STRING ：单个字符串形式的查询字符串（未解析过的形式）。
17. REMOTE_ADDR ：客户端的IP地址。如果服务器使用了nginx 做反向代理或者负载均衡，那么这个值返回的是127.0.0.1 ，这时候可以使用HTTP_X_FORWARDED_FOR 来获取，所以获取ip 地址的代码

```
if request.META.has_key('HTTP_X_FORWARDED_FOR'):
    ip = request.META['HTTP_X_FORWARDED_FOR']
else:
    ip = request.META['REMOTE_ADDR']
```

18. REMOTE_HOST ：客户端的主机名。
19. REQUEST_METHOD ：请求方法。一个字符串类似于GET 或者POST 。
20. SERVER_NAME ：服务器域名。
21. SERVER_PORT ：服务器端口号，是一个字符串类型。

对象常用方法：
1. is_secure() ：是否是采用https 协议。
2. get_host() ：服务器的域名。如果在访问的时候还有端口号，那么会加上端口号。比如
www.baidu.com:9000 。
3. get_full_path() ：返回完整的path。如果有查询字符串，还会加上查询字符串。比如/music/bands/?print=True 。
4. get_raw_uri() ：获取请求的完整url 。



# 2 QueryDict对象：

我们平时用的request.GET 和request.POST 都是QueryDict 对象，这个对象继承自dict ，因此用法跟dict 相差无几。其中用得比较多的是get 方法和getlist 方法。
1. get 方法：用来获取指定key 的值，如果没有这个key ，那么会返回None 。
2. getlist 方法：如果浏览器上传上来的key 对应的值有多个，那么就需要通过这个方法获取








