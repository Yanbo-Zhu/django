
Admin后台系统也称为网站后台管理系统，主要对网站的信息进行管理，如文字、图片、影音和其他日常使用的文件的发布、更新、删除等操作，也包括功能信息的统计和管理，如用户信息、订单信息和访客信息等。
简单来说，它是对网站数据库和文件进行快速操作和管理的系统，以使网页内容能够及时得到更新和调整。


# 1 Django5内置Admin系统初体验


1 


当一个网站上线之后，网站管理员通过网站后台系统对网站进行管理和维护。
Django 已内置Admin后台系统，在创建Django项目的时候，可以从配置文件settings.py中看到项目已默认启用Admin后台系统。


![[08_内置admin系统/images/Pasted image 20240619222511.png]]

---

2
我们浏览器输入http://127.0.0.1:8000/admin/ 即可进入Admin系统首页，默认跳转到Admin系统登录页面。
![[08_内置admin系统/images/Pasted image 20240619222527.png]]

我们发现是英文，我们一般开发交付给客户，必须是本地化中文。我们可以加一个中文本地化的中间件即可实现；

settings.py里加下：
```
# 使用中文
'django.middleware.locale.LocaleMiddleware',
```

![[08_内置admin系统/images/Pasted image 20240619222650.png]]


注意下有顺序要求。
Admin系统用户，权限，认证相关的表有如下6个，其中auth_user是用来存后台管理员信息，默认里面是没有数据的。
![[08_内置admin系统/images/Pasted image 20240619222734.png]]


---
3

我们可以通过python内置的manage.py的createsuperuser 命令来创建超级管理员的账号和密码：
执行python manage.py createsuperuser, 依次输入Username, Email, Password即可
启动服务后，访问http://127.0.0.1:8000/admin/可以看到登录页面，用刚刚设置的 用户名和密码可以登录, 登录进去以后可以完成一些操作。
![[08_内置admin系统/images/Pasted image 20240619222955.png]]


输入 createsuperuser 命令，提示让我们输入用户名，再输入邮箱，以及密码和确认密码，最终我们可以强制输入y，确认。
这样auth_user数据库表有就有管理员数据了。
![[08_内置admin系统/images/Pasted image 20240619223015.png]]

我们回到Admin登录页面，输入刚才创建的用户名和密码：
![[08_内置admin系统/images/Pasted image 20240619223028.png]]


---


点击登录按钮，则进入系统管理主页；
![[08_内置admin系统/images/Pasted image 20240619223040.png]]

在Admin后台系统中可以看到，网页布局分为站点管理、认证和授权、用户和组，分别说明如下:
(1）站点管理是整个Admin后台的主体页面，整个项目的App所定义的模型都会在此页面显示。
(2）认证和授权是Django内置的用户认证系统，包括用户信息、权限管理和用户组设置等功能。
(3）用户和组是认证和授权所定义的模型，分别对应数据表auth_user和 auth_user_groups。


# 2 Django5注册模型到Admin系统

我们开发业务系统的时候，会定义很多的业务模型，我们可以把模型注册到Admin系统，让Admin系统帮我们维护这些模型。也就是在Admin后台自动给模型实现增删改查功能。

注册模型到Admin系统有两个方式，我们都来演示下：
## 2.1 方式一，直接将模型注册到admin后台，以BookTypeInfo模型为例：

打开admin.py，

```
from helloWorld.models import BookTypeInfo
# Register your models here.
# 方法一，将模型直接注册到admin后台
admin.site.register(BookTypeInfo)
```


在后台管理系统注册创建的模型
   ```python
   from django.contrib import admin
   from blog.models import Post, Category, Tag

   # 在应用目录下的 admin.py 文件中，对创建的模型进行注册，可以一起用列表注册，也可以分开注册
   admin.site.register([Post, Category, Tag])
   ```

![[08_内置admin系统/images/Pasted image 20240619223509.png]]


这样admin后台就出现了图书类别信息的管理，我们可以点进去，
![[08_内置admin系统/images/Pasted image 20240619223609.png]]

![[08_内置admin系统/images/Pasted image 20240619223619.png]]

我们可以图书类别信息进行增删改查操作；


## 2.2 方式二：自定义类，继承ModelAdmin，以BookInfo为例


```
# 方法二，自定义类，继承ModelAdmin
@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
	# 设置显示的字段
	list_display = ['id', 'bookName', 'price', 'publishDate', 'bookType']
```

我们可以点进ModelAdmin类里看下，我们可以对模型的增删改查操作做精细化的配置，包括显示字段，分页，可编辑字段，查询字段，排序等

![[08_内置admin系统/images/Pasted image 20240619223704.png]]

Admin后台就多了图书信息
![[08_内置admin系统/images/Pasted image 20240619223719.png]]

![[08_内置admin系统/images/Pasted image 20240619223731.png]]



### 2.2.1 例子2


   ```python
   # 在使用后台管理的时候，可能需要自己定制 admin 的显示内容，可以通过如下进行定制
   @admin.register(Post)
   class PostAdmin(admin.ModelAdmin)
   	list_display = ['title', 'category', 'author'] # 需要展示的字段
   	
   # 或者通过以下方式注册，效果是一样的
   class PostAdmin(admin.ModelAdmin)
   	list_display = ['title', 'category', 'author'] 
   	
   admin.site.register(Post, PostAdmin)

   @admin.register(Category)
   class CategoryAdmin(admin.ModelAdmin)
       # 显示的标签字段，字段不能是 ManyToManyField 类型
       list_display = ('title', 'publisher')
       
   	# 设置每页显示多少条记录，默认是100条
       list_per_page = 20
       
       # 设置默认可编辑字段
       list_editable = ['title', 'author']
       
       # 排除一些不想被编辑的 fields, 没有在列表的不可被编辑
       fields = ('title', 'author')
       
       # 设置哪些字段可以点击进入编辑界面
       list_display_links = ('tag', 'title')
       
       # 进行数据排序，负号表示降序排序
       ordering = ('-id',)
       
       # 显示过滤器
       list_filter = ('author', 'title')
       
       # 显示搜索框，搜索框大小写敏感
       search_fields = ('title',)
       
       # 详细时间分层筛选
       date_hierarchy = 'create_time'
       
       # 增加多选框 filter_horizaontal 和 filter_vertical 作用相同，只是方向不同，只用于
       # ManyToManyField 类型的字段
       filter_horizontal = ('authors',)
       
   # 修改 admin 页面显示标题
   admin.site.site_header = "Blog Manager System"
   # 修改 admin 页面头部标题
   admin.site.site_title = "Blog Manager"
   ```
   修改以后，我们的界面可以看到是以下这样的
![修改后 admin 登录界面](https://upload-images.jianshu.io/upload_images/2888797-0e0472f285e9f4fe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)![admin 管理界面](https://upload-images.jianshu.io/upload_images/2888797-b545b78da9b39a3c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

为了可以和用户进行交流，我们需要获取用户的一些评论之类的，所以我们需要通过表单让用户提交信息，接下来我们将了解下 django 的表单


# 3 Django5内置Admin系统自定义设置

我们在使用Django5的内置Admin系统时会发现一些默认的设置，并不符合我们的业务需求，我们需要自定义设置下；


---

比如模块项目管理这块标题，默认用了模块项目名称，很不好：
![[08_内置admin系统/images/Pasted image 20240619224005.png]]

我们打开helloWorld项目的apps.py，配置类里加下 `verbose_name = '网站图书管理'`
![[08_内置admin系统/images/Pasted image 20240619224032.png]]

这样我们会发现，用户体验好多了；
![[08_内置admin系统/images/Pasted image 20240619224214.png]]


---


还有一个地方，网站标题和子标题，也不友好。
![[08_内置admin系统/images/Pasted image 20240619224227.png]]


我们可以打开admin.py，设置如下：
```
# 设置网站标题和应用标题
admin.site.site_title = '锋哥后台管理'
admin.site.index_title = '图书管理模块'
```


---

![[08_内置admin系统/images/Pasted image 20240619224337.png]]

我们可以通过在admin.py设置 admin.site.site_header 实现；

admin.site.site_header = "python222网站管理系统"
![[08_内置admin系统/images/Pasted image 20240619225204.png]]



