
# 1 基本配置 


Django 的配置文件 settings.py用于配置整个网站的环境和功能，核心配置必须有项目路径、密钥配置、域名访问权限、App列表、中间件、资源文件、模板配置、数据库的连接方式

```
# 项目路径
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# 密钥配置
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^+$)&&p^atzo)&ytg&8%6dq!!ujgh7t2w#2n^i_f#r^#*vyqh'

# 调试模式
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 域名访问权限
ALLOWED_HOSTS = []


# Application definition
# APP列表
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'helloWorld.apps.HelloworldConfig'
]


```

- BASE_DIR 项目路径：主要通过os模块读取当前项目在计算机系统的具体路径，该代码在创建项目时自动生成，一般情况下无须修改。
- SECRET_KEY 密钥配置：密钥配置SECRET_KEY:这是一个随机值，在项目创建的时候自动生成，一般情况下无须修改。主要用于重要数据的加密处理，提高项目的安全性，避免遭到攻击者恶意破坏。密钥主要用于用户密码、CSRF机制和会话Session等数据加密。
    - 用户密码: Django 内置一套Auth认证系统，该系统具有用户认证和存储用户信息等功能，在创建用户的时候，将用户密码通过密钥进行加密处理，保证用户的安全性。
    - CSRF机制:该机制主要用于表单提交，防止窃取网站的用户信息来制造恶意请求。
    - 会话Session: Session的信息存放在Cookie中，以一串随机的字符串表示，用于标识当前访问网站的用户身份，记录相关用户信息。
- DEBUG 调试模式：该值为布尔类型。如果在开发调试阶段，那么应设置为True，在开发调试过程中会自动检测代码是否发生更改，根据检测结果执行是否刷新重启系统。如果项目部署上线，那么应将其改为False，否则会泄漏项目的相关信息。
- ALLOWED_HOSTS 域名访问权限：设置可访问的域名,默认值为空列表。当DEBUG为True并且ALLOWED_HOSTS为空列表时，项目只允许以localhost或127.0.0.1在浏览器上访问。当DEBUG为False时，ALLOWED_HOSTS为必填项，否则程序无法启动，如果想允许所有域名访问，可设置`ALLOW_HOSTS=['*']`。
- INSTALLED_APPS APP列表：告诉Django有哪些App。在项目创建时已有admin、auth和sessions等配置信息，这些都是Django内置的应用功能，各个功能说明如下。
    1. admin:内置的后台管理系统。
    2. auth:内置的用户认证系统。
    3. contenttypes:记录项目中所有model元数据( Django 的ORM框架)。
    4. sessions: Session会话功能，用于标识当前访问网站的用户身份，记录相关用户信息。
    5. messages:消息提示功能。
    6. staticfiles:查找静态资源路径。

如果在项目中创建了App，就必须在App列表INSTALLED_APPS 添加App类

# 2 资源文件配置


资源文件配置分为静态资源和媒体资源。静态资源的配置方式由配置属性STATIC_URL、STATICFILES DIRS和STATIC_ROOT进行设置;媒体资源的配置方式由配置属性MEDIA_URL和MEDIA ROOT决定

## 2.1 静态资源配置=STATIC_URL
静态资源指的是网站中不会改变的文件。在一般的应用程序中，静态资源包括CSS文件、JavaScript文件以及图片等资源文件。
默认配置，app下的static目录为静态资源，可以直接访问。其他目录不行。
`STATIC_URL = 'static/'`

通过测试说明，也就app下的static目录下的静态资源才能访问。

再试试app下的images目录下的qq.jpg, 404 not found 
最后再测试下项目目录下的static下的pig.jpg, 404 not found


## 2.2 静态资源集合配置-STATICFILES DIRS


由于STATIC_URL的特殊性，在开发中会造成诸多不便，比如将静态文件夹存放在项目的根目录以及定义
多个静态文件夹等。我们可以通过配置STATICFILES DIRS实现多个目录下的静态资源可以访问。

```
# 设置静态资源文件集合
STATICFILES_DIRS = [BASE_DIR / "static", BASE_DIR / "helloWorld/images"]
```

我们再测试下：  这些目录下的就都可以访问了



## 2.3 静态资源部署配置-STATIC_ROOT

静态资源配置还有STATIC_ROOT，其作用是在服务器上部署项目，实现服务器和项目之间的映射。
STATIC_ROOT 主要收集整个项目的静态资源并存放在一个新的文件夹，然后由该文件夹与服务器之间构建映射关系。STATIC_ROOT配置如下:
```
# 静态资源部署
STATIC_ROOT = BASE_DIR / 'static'
```


当项目的配置属性 DEBUG 设为True的时候，Django 会自动提供静态文件代理服务，此时整个项目处于开发阶段，因此无须使用STATIC_ROOT。当配置属性DEBUG 设为False的时候，意味着项目进入生产环境，Django不再提供静态文件代理服务，此时需要在项目的配置文件中设置STATIC_ROOT。


设置STATIC_ROOT需要使用 Django操作指令collectstatic来收集所有静态资源，这些静态资源都会保存在STATIC_ROOT所设置的文件夹里。


## 2.4 媒体资源配置-MEDIA
一般情况下，STATIC_URL是设置静态文件的路由地址，如CSS样式文件、JavaScript文件以及常用图片等。对于一些经常变动的资源，通常将其存放在媒体资源文件夹，如用户头像、歌曲文件等

媒体资源和静态资源是可以同时存在的，而且两者可以独立运行，互不影响，而媒体资源只有配置属性MEDIA_URL和 MEDIA_ROOT。

我们在项目目录下新建media目录，里面再放一个boy.jpg图片

然后在配置文件settings.py里设置配置属性MEDIA_URL和 MEDIA_ROOT，MEDIA_URL用于设置媒体资源的路由地址，MEDIA_ROOT用于获取 media文件夹在计算机系统的完整路径信息，如下所示：


```
# 设置媒体路由
MEDIA_URL = 'media/'
# 设置media目录的完整路径
MEDIA_ROOT = BASE_DIR / 'media'
```


配置属性设置后，还需要将media文件夹注册到 Django里，让 Django知道如何找到媒体文件，否则无法在浏览器上访问该文件夹的文件信息。打开项目文件夹的urls.py文件，为媒体文件夹media添加相应的路由地址，代码如下:

```
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

import helloWorld.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', helloWorld.views.index),
    
    # 配置媒体文件的路由地址
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT},name='media')
]
```


`http://127.0.0.1:8000/media/boy.jpg`

# 3 模版配置

在 Web开发中，模板是一种较为特殊的HTML文档。这个HTML文档嵌入了一些能够让Django识别的变量和指令，然后由Django的模板引擎解析这些变量和指令，生成完整的HTML网页并返回给用户浏览。

模板是Django里面的MTV框架模式的T部分，配置模板路径是告诉Django在解析模板时，如何找到模板所在的位置。创建项目时，Django已有初始的模板配置信息，如下所示:

```
TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates']
    ,
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


模板配置是以列表格式呈现的，每个元素具有不同的含义，其含义说明如下。
- BACKEND:定义模板引擎，用于识别模板里面的变量和指令。内置的模板引擎有 DjangoTemplates和 jinja2.Jinja2，每个模板引擎都有自己的变量和指令语法。
- DIRS:设置模板所在路径，告诉Django在哪个地方查找模板的位置，默认为空列表。
- APP_DIRS:是否在App里查找模板文件。
- OPTIONS:用于填充在RequestContext 的上下文（模板里面的变量和指令)，一般情况下不做任何修改。


我们是可以在应用里新建templates，供自己的应用使用。在templates下新建index2.html模版文件
![](images/Pasted%20image%2020240619000953.png)

views.py里面把index.html改成index2.html
![](images/Pasted%20image%2020240619001003.png)


最后就是在DIRS里面加上应用的模版路径即可。
![](images/Pasted%20image%2020240619001013.png)


启动测试
http://127.0.0.1:8000/index/


但是我们这里有个疑问，如果说应用里的模版和项目里的模版名字一样，起冲突了。这时候，会选择哪个呢，或者说哪个优先级高？

我们测试下吧。把应用里的index2.html改成index.html，以及views.py里面也改下
![](images/Pasted%20image%2020240619001159.png)

然后我们重新运行测试：运行结果显示的是项目里的模版。
![](images/Pasted%20image%2020240619001205.png)


锋哥经过查看Django底层源码，其实优先级顺序是根据模版配置的目录顺序来定的，我们前面项目模版在前面，所以就显示项目模版。

如果我们把应用模版配置路径放前面

![](images/Pasted%20image%2020240619001221.png)

# 4 数据库配置 

数据库配置是选择项目所使用的数据库的类型，不同的数据库需要设置不同的数据库引擎，数据库引擎
用于实现项目与数据库的连接，Django提供4种数据库引擎:
'django.db.backends.postgresql'
'django.db.backends.mysql'
'django.db.backends.sqlite3'
'django.db.backends.oracle'

项目创建时默认使用Sqlite3数据库，这是一款轻型的数据库，常用于嵌入式系统开发，而且占用的资源非常少。Sqlite3数据库配置信息如下:

```
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}
```


如果要把上述的连接信息改成MySQL数据库，首先需要安装MySQL连接模块 mysqlclient
`pip install mysqlclient -i https://pypi.tuna.tsinghua.edu.cn/simple`


mysqlclient模块安装后，在项目的配置文件settings.py中配置MySQL数据库连接信息
```
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'db_python222',
'USER': 'root',
'PASSWORD': '123456',
'HOST': 'localhost',
'PORT': '3306'
}
}
```
（django5至少需要MySQL 8.0.11版本）

我们来测试下数据库连接；
我们首先在mysql 里创建数据库db_python222
然后我们用Django5 manage.py 提供的内置命令 migrate 来创建Django内置功能的数据表；
![](images/Pasted%20image%2020240619001350.png)


刷新数据库表 
![](images/Pasted%20image%2020240619001413.png)


这些是Django内置自带的Admin后台管理系统，Auth用户系统以及会话机制等功能需要用到的表。

注意：django也支持pymysql,mysqldb等，但是用的时候会有点小问题，所以建议大家还是用
mysqlclient，比较稳定。

## 4.1 多数据库 



例如上面，我们定义了三个数据库，两个mysql，一个sqlite；配置属性DATABASES设有3个键值对，分别是：'default'，'mySqlite3'，'mySql3'，每个键值对代表Django连接了某个数据库。

若项目中连接了多个数据库，则数据库之间的使用需要遵从一定的规则和设置。比如项目中定义了多个模型，每个模型所对应的数据表可以选择在某个数据库中生成，如果模型没有指向某个数据库，模型就会在key为default的数据库里生成。


```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_python222',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3308'
    },
    'mySqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'mySql3': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_django',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```



# 5 中间件
中间件(Middleware）是一个用来处理 Django 的请求(Request）和响应（Response）的框架级别的钩子，它是一个轻量、低级别的插件系统，用于在全局范围内改变 Django的输入和输出。


当用户在网站中进行某个操作时，这个过程是用户向网站发送HTTP请求(Request);而网站会根据用户的操作返回相关的网页内容，这个过程称为响应处理(Response)。从请求到响应的过程中，当 Django接收到用户请求时，首先经过中间件处理请求信息，执行相关的处理，然后将处理结果返回给用户。


![](images/Pasted%20image%2020240619001811.png)


django默认的中间配置如下：

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

django自带的中间件有：
SecurityMiddleware:内置的安全机制，保护用户与网站的通信安全。
SessionMiddleware:会话Session功能。
LocaleMiddleware:国际化和本地化功能。
CommonMiddleware:处理请求信息，规范化请求内容。
CsrfViewMiddleware:开启CSRF防护功能。
AuthenticationMiddleware:开启内置的用户认证系统。
MessageMiddleware:开启内置的信息提示功能。
XFrameOptionsMiddleware:防止恶意程序单击劫持。


我们也可以自定义中间件：

中间件可以定义五个方法，分别是：（主要的是process_request和process_response），在自己定义
- 中间件时，必须继承MiddlewareMixin
- process_request(self,request) 请求views方法之前会执行。
- process_view(self, request, callback, callback_args, callback_kwargs) Django会在调用视图函数之前调用process_view方法。
- process_template_response(self,request,response) 该方法对视图函数返回值有要求，必须是一个含有render方法类的对象，才会执行此方法
- process_exception(self, request, exception) 这个方法只有在视图函数中出现异常了才执行
- process_response(self, request, response) 请求执行完成，返回页面前会执行


新建Md1自定义中间件类，继承MiddlewareMixin，实现process_request和process_response方法。
``
![](images/Pasted%20image%2020240619002020.png)

```
"""
自定义中间件
作者 : 小锋老师
官网 : www.python222.com
"""
from django.utils.deprecation import MiddlewareMixin

class Md1(MiddlewareMixin):
    def process_request(self, request):
        print("request请求来了")

    def process_response(self, request, response):
        print("请求处理完毕，将返回到页面")
        return response
```


setting.py里配置自定义中间件。

![](images/Pasted%20image%2020240619002142.png)


views.py的index请求处理方法，我们加一句打印。
![](images/Pasted%20image%2020240619002154.png)

最后我们运行测试：
```
http://127.0.0.1:8000/index/

request请求来了
页面请求处理中
请求处理完毕，将返回到页面


```

# 6 其他配置 


还有一些其他settings.py配置我们了解下
ROOT_URLCONF = 'python222_site1_pc.urls' 它指定了当前项目的根 URL，是 Django 路由系统的入口。

WSGI_APPLICATION = 'python222_site1_pc.wsgi.application' 项目部署时，Django 的内置服务器将

使用的 WSGI 应用程序对象的完整 Python 路径

AUTH_PASSWORD_VALIDATORS 这是一个支持插拔的密码验证器，且可以一次性配置多个，Django通过这些内置组件来避免用户设置的密码等级不足的问题。

LANGUAGE_CODE = 'en-us' TIME_ZONE = 'UTC'
分别代表语言配置项和当前服务端时区的配置项，我们常用的配置如下所示：
- LANGUAGE_CODE 取值是英文：'en-us'或者中文：'zh-Hans'；
- TIME_ZONE 取值是世界时区 'UTC' 或中国时区 'Asia/Shanghai'。

USE_I18N = True 项目开发完成后，可以选择向不同国家的用户提供服务，那么就需要支持国际化和本地化。

USE_TZ = True 它指对时区的处理方式，当设置为 True 的时候，存储到数据库的时间是世界时间 'UTC'。

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 默认主键自增类型


## 6.1 基础配置（中文）

通过上面的配置，你看到的界面应该是英文的，并且时区也是UTC时区。所以我们需要进一步配置。

在settings中有如下配置:
    LANGUAGE_CODE = 'zh-hans'  # 语言
    TIME_ZONE = 'Asia/Shanghai'  # 时区
    USE_I18N = True  # 语言
    USE_L10N = True  # 数据和时间格式
    USE_TZ = True  # 启用时区

修改完这些之后，刷新下试试。你可以尝试修改上面的配置，看看分别对应什么功能。

到这一部分我们基本上完成了admin的部分。下一节我们来完成页面提交数据的部分，看下如何使用Form。


---
汉化 

在`MIDDLEWARE`部分，增加`django.middleware.locale.LocaleMiddleware`，代码如下：

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]
```

刷新下界面，是不是变成汉字了。

国际化支持在 Django 中做得是非常的出色，程序可以国际化，模板可以国际化，甚至js都可以国际化。这一点其它的类似框架都还做不到。而国际化的支持更是 RoR 的一个弱项，甚至在 [Snakes and Rubies](http://snakesandrubies.com/event) 的会议上，RoR 的作者都不想支持国际化。但 Django 却做得非常出色，目前已经有二十多种语言译文。


