
HTTP是一种无状态协议，每次客户端访问web页面时，客户端打开一个单独的浏览器窗口连接到web服务器，由于服务器不会自动保存之前客户端请求的相关信息，所有无法识别一个HTTP请求是否为第一次访问。这就引进了web客户端和服务器端之间的会话，这就是会话管理。常用的会话跟踪技术是Cookie与Session。Cookie通过在客户端记录信息确定用户身份，Session通过在服务器端记录信息确定用户身份


# 1 介绍

## 1.1 cookie
在网站中，http请求是无状态的。也就是说即使第一次和服务器连接后并且登录成功后，第二次请求服务器依然不能知道当前请求是哪个用户。cookie 的出现就是为了解决这个问题，第一次登录后服务器返回一些数据（cookie）给浏览器，然后浏览器保存在本地，当该用户发送第二次请求的时候，就会自动的把上次请求存储的cookie 数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前用户是哪个了。

cookie是某些网站为了辨别用户身份，进行Session跟踪而储存在用户本地终端上的数据（通常经过加密），由用户客户端计算机暂时或永久保存的信息。

Cookie定义了一些HTTP请求头和HTTP响应头，通过这些HTTP头信息使服务器可以与客户进行状态交互。

客户端请求服务器后，如果服务器需要记录用户状态，服务器会在响应信息中包含一个Set-Cookie的响应头，客户端会根据这个响应头存储Cookie信息。再次请求服务器时，客户端会在请求信息中包含一个Cookie请求头，而服务器会根据这个请求头进行用户身份、状态等较验。


cookie 中包含有 userID
cookie 存储的数据量有限，不同的浏览器有不同的存储大小，但一般不超过4KB。因此使用cookie 只能存储一些小量的数据。

![[05_视图View/images/Pasted image 20240619160009.png]]

## 1.2 session

session和cookie的作用有点类似，都是为了存储用户相关的信息。不同的是， cookie 是存储在本地浏览器， session 是一个思路、一个概念、一个服务器存储授权信息的解决方案，不同的服务器，不同的框架，不同的语言有不同的实现。虽然实现不一样，但是他们的目的都是服务器为了方便存储数据的。session 的出现，是为了解决cookie 存储数据不安全的问题的。

通常 session 是存储在 服务器端的 


Session是另一种记录客户状态的机制，不同的是Cookie保存在客户端浏览器中，而Session保存在服务器上。客户端浏览器访问服务器的时候，服务器把客户端信息以某种形式记录在服务器上。这就是Session。客户端浏览器再次访问时只需要从该Session中查找该客户的状态就可以了。

当程序需要为某个客户端的请求创建一个session的时候，服务器首先检查这个客户端的请求里是否已包含了一个session标识，称为session id，如果已包含一个session id则说明以前已经为此客户端创建过session，服务器就按照session id把这个session检索出来使用（如果检索不到，可能会新建一个），如果客户端请求不包含session id，则为此客户端创建一个session并且生成一个与此session相关联的 session id，session id的值应该是一个既不会重复，又不容易被找到规律以仿造的字符串，这个 session id将被在本次响应中返回给客户端保存。

![[05_视图View/images/Pasted image 20240619160203.png]]


## 1.3 cookie和session使用

web 开发发展至今， cookie 和session 的使用已经出现了一些非常成熟的方案。在如今的市场或者企业里，一般有两种存储方式：

1 存储在服务端：
通过cookie 存储一个sessionid ，然后具体的数据则是保存在session中。如果用户已经登录，则服务器会在cookie 中保存一个sessionid ，下次再次请求的时候，会把该sessionid 携带上来，服务器根据sessionid 在session 库中获取用户的
session 数据。就能知道该用户到底是谁，以及之前保存的一些状态信息。这种专业术语叫做 server side session 。Django 把session 信息默认存储到数据库中，当然也可以存储到其他地方，比如缓存中，文件系统中等。存储在服务器的数据会更加的安全，不容易被窃取。
但存储在服务器也有一定的弊端，就是会占用服务器的资源，但现在服务器已经发展至今，一些session 信息还是绰绰有余的。

2 将session 数据加密，然后存储在cookie 中: 
这种专业术语叫做client side session 。 flask 框架默认采用的就是这种方式，但是也可以替换成其他形式。

## 1.4 Session和Cookie的区别

1、数据存储位置：cookie 数据存放在客户的浏览器上，session 数据放在服务器上。
2、安全性：cookie不是很安全，别人可以分析存放在本地的cookie并进行cookie欺骗，考虑到安全应当使用session。
3、服务器性能：session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能，考虑到减轻服务器性能方面，应当使用cookie。
4、数据大小：单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie。
5、信息重要程度：可以考虑将用户信息等重要信息存放为session，其他信息如果需要保留，可以放在cookie中。




# 2 在django中操作cookie

## 2.1 设置cookie: response.set_cookie 

是设置值给浏览器的。因此我们需要通过response 的对象来设置，设置cookie 可以通过response.set_cookie 来设置，这个方法的相关参数如下：
1. key ：这个cookie 的key 。
2. value ：这个cookie 的value 。
3. max_age ：最长的生命周期。单位是秒。
4. expires ：过期时间。跟max_age 是类似的，只不过这个参数需要传递一个具体的日期，比如 datetime 或者是符合日期格式的字符串。如果同时设置了expires 和max_age ，那么将会使用expires 的值作为过期时间。
5. path ：对域名下哪个路径有效。默认是对域名下所有路径都有效。
6. domain ：针对哪个域名有效。默认是针对主域名下都有效，如果只要针对某个子域名才有效，那么可以设置这个属性.
7. secure ：是否是安全的，如果设置为True ，那么只能在https 协议下才可用。
8. httponly ：默认是False 。如果为True ，那么在客户端不能通过JavaScript 进行操作。


```
def add_cookie(request):
    response = HttpResponse('设置cookie')
    max_age = 60*60*24*7
    response.set_cookie('username', 'zhiliao', max_age=max_age)
    return response
```



```
获取HttpResponse对象
# rep = HttpResponse(...)
rep ＝ render(request, ...)
# 设置 cookie
rep.set_cookie(key,value,...)
rep.set_signed_cookie(key,value,salt='加密盐', max_age=None, ...)

参数
key, 键
value='', 值
max_age=None, 超时时间
expires=None, 超时时间(IE requires expires, so set it if hasn't been already.)
path='/', Cookie生效的路径，/ 表示根路径，特殊的：根路径的cookie可以被任何url的页面访
问
domain=None, Cookie生效的域名
secure=False, https传输
httponly=False 只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被
覆盖）
```

## 2.2 删除cookie 

通过delete_cookie 即可删除cookie 。实际上删除cookie 就是将指定的cookie 的值设置为空的字符串，然后使用将他的过期时间设置为0 ，也就是浏览器关闭后就过期。

```
def delete_cookie(request):  
    response = HttpResponse("删除cookie")  
    response.delete_cookie('username')  
    return response  
```

```
# 获取HttpResponse对象
# rep = HttpResponse(...)
rep ＝ render(request, ...)
# 删除 cookie
rep.delete_cookie(key)
此方法会删除用户浏览器上之前设置的cookie值

```


## 2.3 获取cookie

获取浏览器发送过来的cookie 信息。可以通过request.COOKIES 来或者。这个对象是一个字典类型。
比如获取所有的cookie ，那么示例代码如下：


```
cookies = request.COOKIES
for cookie_key,cookie_value in cookies.items():
print(cookie_key,cookie_value)
```


```python
def get_cookie(request):  
     username = request.COOKIES.get('username')  
     print(username)    
     
     for key, value in request.COOKIES.items():  
        print(key, value)  
     return HttpResponse("get cookie")  
```

![](05_视图View/images/Pasted%20image%2020240618221910.png)

---

```
request.COOKIES['key']
request.COOKIES.get('key')
这俩个方法可以获取指定键名的cookie
request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
default: 默认值
salt: 加密盐
max_age: 后台控制过期时间，默认是秒数
expires: 专门针对IE浏览器设置超时时间
```


# 3 在Django中操作session


django 中的session 默认情况下是存储在服务器的数据库中的，在表中会根据sessionid 来提取指定 的session 数据，然后再把这个sessionid 放到cookie 中发送给浏览器存储.  浏览器下次在向服务器发送请求的时候会自动的把所有cookie 信息都发送给服务器，服务器再从cookie 中获取sessionid ，然后再从数据库中获取session 数据。


seesions 模型 是报错在 urls.py中 INSTALLED_APPS 中的 django.contib.sessions 中的 

![](05_视图View/images/Pasted%20image%2020240618222631.png)


![](05_视图View/images/Pasted%20image%2020240618223111.png)

![](05_视图View/images/Pasted%20image%2020240618223149.png)



```
1. 获取、设置、删除Session中数据
request.session['k1'] # 没有值会报错
request.session.get('k1',None) # 可以获取多组
request.session['k1'] = 123 # 可以设置多组
request.session.setdefault('k1',123) # 存在则不设置
del request.session['k1']

2. 所有 键、值、键值对
request.session.keys()
request.session.values()
request.session.items()
request.session.iterkeys()
request.session.itervalues()
request.session.iteritems()

4. 会话session的key
request.session.session_key
5. 将所有Session失效日期小于当前日期的数据删除
request.session.clear_expired()
6. 检查会话session的key在数据库中是否存在
request.session.exists("session_key")
7. 删除当前会话的所有Session数据
request.session.delete() # 只删客户端
8. 删除当前的会话数据并删除会话的Cookie。
request.session.flush() # 服务端、客户端都删
这用于确保前面的会话数据不可以再次被用户的浏览器访问
例如，django.contrib.auth.logout() 函数中就会调用它。

9. 设置会话Session和Cookie的超时时间
'django默认的session失效时间是14天'
request.session.set_expiry(value)
* 如果value是个整数，session会在些秒数后失效。
* 如果value是个datatime或timedelta，session就会在这个时间后失效。
* 如果value是0,用户关闭浏览器session就会失效。
* 如果value是None,session会依赖全局session失效策略。
```


# 4 Django 中的 Session 配置
```
1. 数据库Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db' # 引擎（默认）

2. 缓存Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache' # 引擎
SESSION_CACHE_ALIAS = 'default' # 使用的缓存别名（默认内存
缓存，也可以是memcache），此处别名依赖缓存的设置

3. 文件Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file' # 引擎
SESSION_FILE_PATH = None # 缓存文件路径，如果为
None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()

4. 缓存+数据库
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db' # 引擎

5. 加密Cookie Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies' # 引擎
其他公用设置项：
SESSION_COOKIE_NAME ＝ "sessionid" # Session的cookie保存在浏览器上时的key，
即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH ＝ "/" # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600 # Session的cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False # 是否每次请求都保存Session，默认修改之后才保
存（默认）


```

# 5 通过request.session处理 

但是我们在操作session 的时候，这些细节压根就不用管。我们只需要通过request.session 即可操作

```
def index(request):
    request.session.get('username')
    return HttpResponse('index')
```

session 常用的方法如下：
1. get ：用来从session 中获取指定值。
2. pop ：从session 中删除一个值。
3. keys ：从session 中获取所有的键。
4. items ：从session 中获取所有的值。
5. clear ：清除当前这个用户的session 数据。
6. flush ：删除session 并且删除在浏览器中存储的session_id ，一般在注销的时候用得比较多。
7. set_expiry(value) ：设置过期时间。
    1. 整形：代表秒数，表示多少秒后过期。
    2. 0 ：代表只要浏览器关闭， session 就会过期。session_id 会被自动删除 
    3. None ：会使用全局的session 配置。在settings.py 中可以设置SESSION_COOKIE_AGE 来配置全局的过期时间。默认是1209600 秒，也就是2周的时间
8. clear_expired ：清除过期的session 。Django 并不会清除过期的session ，需要定期手动的清理，或者是在终端，使用命令行python manage.py clearsessions 来清除过期的session


# 6 修改session的存储机制

默认情况下， session 数据是存储到数据库中的。当然也可以将session 数据存储到其他地方。可以通过设置SESSION_ENGINE 来更改session 的存储位置，这个可以配置为以下几种方案：
1. django.contrib.sessions.backends.db ：使用数据库。默认就是这种方案。
2. django.contrib.sessions.backends.file ：使用文件来存储session。
3. django.contrib.sessions.backends.cache ：使用缓存来存储session。想要将数据存储到缓存中，前提是你必须要在settings.py 中配置好CACHES ，并且是需要使用Memcached ，而不能使用纯内存作为缓存。
4. django.contrib.sessions.backends.cached_db ：在存储数据的时候，会将数据先存到缓存中，再存到数据库中。这样就可以保证万一缓存系统出现问题，session数据也不会丢失。在获取数据的时候，会先从缓存中获取，如果缓存中没有，那么就会从数据库中获取。
5. django.contrib.sessions.backends.signed_cookies ：将session 信息加密后存储到浏览器的cookie 中。这种方式要注意安全，建议设置SESSION_COOKIE_HTTPONLY=True ，那么在浏览器中不能通过js 来操作session 数据，并且还需要对settings.py 中的SECRET_KEY 进行保密，因为一旦别人知道这个SECRET_KEY ，那么就可以进行解密。另外还有就是在cookie 中，存储的数据不能超过4k 。


# 7 例子 

## 7.1 例子1 

urls.py
```python
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('cookie/add', views.add_cookie, name='add cookie'),  
    path('cookie/delete', views.delete_cookie, name='delete cookie'),  
    path('cookie/get', views.get_cookie, name='get cookie'),  
    path('session/add', views.add_session, name='add session'),  
    path('session/get', views.get_session, name='get session')  
]
```


views.py
```python
from django.shortcuts import HttpResponse  
  
  
def add_cookie(request):  
    response = HttpResponse('设置cookie')  
    max_age = 60*60*24*7  
    response.set_cookie('username', 'zhiliao', max_age=max_age)  
    return response  
  
  
def delete_cookie(request):  
    response = HttpResponse("删除cookie")  
    response.delete_cookie('username')  
    return response  
  
  
def get_cookie(request):  
    # username = request.COOKIES.get('username')  
    # print(username)    for key, value in request.COOKIES.items():  
        print(key, value)  
    return HttpResponse("get cookie")  
  
  
def add_session(request):  
    # 如果没有设置session过期时间，默认是2周后过期  
    request.session['user_id'] = 'zhiliao'  
    # 如果设置成0，那么浏览器关闭后，session就会过期  
    request.session.set_expiry(0)  
    return HttpResponse("session add")  
  
  
def get_session(request):  
    username = request.session.get('user_id')  
    print(username)  
    return HttpResponse('get session')
```


## 7.2 例子2

下面通过一个具体Django事例来深入体验下Django项目里的Cookie&Session操作

views.py里定义两个方法，分别是登录页面跳转，以及登录逻辑处理
```python
def to_login(request):
	"""
	跳转登录页面
	:param request:
	:return:
	"""
	return render(request, 'login.html')`

def login(request):
	"""
	登录
	:param request:
	:return:
	"""
	user_name = request.POST.get("user_name")
	pwd = request.POST.get("pwd")
	if user_name == 'python222' and pwd == '123456':
		request.session['currentUserName'] = user_name # session中存一个用户名
		print('session获取', request.session['currentUserName'])
		response = render(request, 'main.html') # 获取HttpResponse
		response.set_cookie("remember_me", True) # 设置cookie
		return response
	else:
		content_value = {"error_info": '用户名或者密码错误！'}
		return render(request, 'login.html', context=content_value)
```

urls.py里定义映射：
```
path('toLogin/', helloWorld.views.to_login),
path('login', helloWorld.views.login)
```


templates下新建login.html和main.html
login.html
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>登录页面</title>
    </head>
    <body>
        <form action="/login" method="post">
            {% csrf_token %}
            <table>
                <tr>
                    <th>用户登录</th>
                </tr>
                <tr>
                    <td>用户名：</td>
                    <td><input type="text" name="user_name" /></td>
                </tr>
                <tr>
                    <td>密码：</td>
                    <td><input type="password" name="pwd" /></td>
                </tr>
                <tr>
                    <td>
                        main.html 测试运行，浏览器输入： http://127.0.0.1:8000/toLogin/ 转发到login.html 我们先输入一个错误的用户名和密码：
                        <input type="submit" value="提交" />
                    </td>
                </tr>
                <tr>
                    <td colspan="2"><font color="red">{{ error_info }}</font></td>
                </tr>
            </table>
        </form>
    </body>
</html>

```

main.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>主页面</title>
</head>
<body>
欢迎：{{ request.session.currentUserName }}
</body>
</html>
```


测试运行，浏览器输入： http://127.0.0.1:8000/toLogin/
![[05_视图View/images/Pasted image 20240619161353.png]]

转发到login.html
我们先输入一个错误的用户名和密码：

![[05_视图View/images/Pasted image 20240619161447.png]]

![[05_视图View/images/Pasted image 20240619161457.png]]

携带错误信息参数，转发到登录页面，页面提示错误信息。


我们在输入一个正确的用户名和密码：，则转发到main.html主页面。
![[05_视图View/images/Pasted image 20240619161516.png]]
![[05_视图View/images/Pasted image 20240619161527.png]]

同时服务器返回set-cookies信息，包括内置的sessionid以及我们自己设置的remember_me。
![[05_视图View/images/Pasted image 20240619161548.png]]



