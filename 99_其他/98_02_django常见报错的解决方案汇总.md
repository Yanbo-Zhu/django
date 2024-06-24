
# 1 报错：djanog xxx doesn’t declare an explicit app_label and isn’t in an application

## 1.1 解决方案01(INSTALLED_APPS)

报错举例：Runtime Error: Model class addresstest.models.address_info doesn’t declare an explicit app_label and isn’t in an application in INSTALLED_APPS.

解决: 需要在 settings.py 中的INSTALLED_APPS 添加 app包名称： addresstest

参考：django:doesn’t declare an explicit app_label and isn’t in an application in INSTALLED_APPS.:https://blog.csdn.net/wang603603/article/details/86932856

## 1.2 解决方案02(django.contrib.sites)

在settings.py中增加

```
INSTALLED_APPS = [
	...
	'django.contrib.sites',
]
```

参考:doesn’t declare an explicit app_label and isn’t in an application in INSTALLED_APPS.:https://www.cnblogs.com/crave/p/11043786.html

## 1.3 解决方案03(import path)

补充import为完整路径

`from models import User => from users.models import User`

参考:Django开发BUG记录—RuntimeError: Model class models.User doesn’t declare an explicit app_label and isn’:https://www.pianshen.com/article/743343293/

## 1.4 解决方案04(abs_path)

从绝对路径导包会报错,改为相对路径

```
# from meiduo.apps.users import views

from . import views
urlpatterns=[]
```

参考:Django项目一个小错误doesn’t declare an explicit app_label:https://blog.csdn.net/u011519550/article/details/82354262

## 1.5 解决方案05(我的方案)(pycharm auto import problem)

将from xxx.yy.zz import 改为 from zz import 
原因 python manage.py启动时：python /xxx/yyy/zz.py。 会自动加入sys.path：/xxx/yyy/  ,  导致pycharm自动提示import路径不完全正确，从而django的model的import会尝试定位名为yy.zz的app，实际app_name是zz

简单来说就是pycharm自动提示import路径有误的问题。修改后pycharm提示代码有误，但实际可正确执行
