

![](images/Pasted%20image%2020240618232004.png)


指令说明
changepassword 修改内置用户表的用户密码
createsuperuser 为内置用户表创建超级管理员账号
remove_stale_contenttypes 删除数据库中已不使用的数据表
check 检测整个项目是否存在异常问题
compilemessages 编译语言文件，用于项目的区域语言设置
createcachetable 创建缓存数据表，为内置的缓存机制提供存储功能
dbshell 进入Django配置的数据库，可以执行数据库的SOL语句
diffsettings 显示当前settings.py的配置信息与默认配置的差异
dumpdata 导出数据表的数据并以JSON格式存储，如 python manage.py
dumpdata index >data.json，这是index的模型所对应的数据导 出，并保存在 data.json文件中
flush 清空数据表的数据信息
inspectdb 获取项目所有模型的定义过程
loaddata 将数据文件导入数据表，如 python manage.py loaddatadata.,json
makemessages 创建语言文件，用于项目的区域语言设置
makemigrations 从模型对象创建数据迁移文件并保存在App 的migrations文件夹
migrate 根据迁移文件的内容，在数据库里生成相应的数据表
sendtestemail 向指定的收件人发送测试的电子邮件
shell 进入Django的Shell模式,用于调试项目功能
showmigrations 查看当前项目的所有迁移文件
sqlflush 查看清空数据库的SOL语句脚本
sqlmigrate 根据迁移文件内容输出相应的SQL语句
sqlsequencereset 重置数据表递增字段的索引值
squashmigrations 对迁移文件进行压缩处理
startapp 创建项目应用App
optimizemigration 允许优化迁移操作
startproject 创建新的Django项目
test 运行App里面的测试程序
testserver 新建测试数据库并使用该数据库运行项目
clearsessions 清除会话Session数据
collectstatic 收集所有的静态文件
findstatic 查找静态文件的路径信息
runserver 在本地计算机上启动Django项目


# 1 makemigrations

makemigrations是django中的常用操作，但是坑也比较多。

坑的主要原因，使用django的manage.py makemigrations，django会加载整个项目，而不仅仅是models.py。而这会引发一系列问题。


## 1.1 凡是makemigrations相关问题，有解决的套路

1，如果只修改了部分app则makemigrations和migrate都指定具体app，避免全部app的扫描和更新。降低失败概率。

2，如果修改的app生成表失败，或者和预想不一致，则删除django_migrations数据表中有问题app相关记录，重新makemigrations+migrate生成（数据会丢失，线上别这么干就行了）

## 1.2 初次初始化时使用了未（来得及）创建的表

比如：缓存类型对象查询到表，报错，进而导致无法执行makemigrations（无法创建对象表）类似先有鸡先有蛋矛盾。

比如:
```
views.py
member_buffer=Member.objects.all()
```

本意是为了当做类似缓存使用（就这意思，代码对没对不重要），但是makemigrations之前是没有表Member的，

要创建表Member就好扫描到views.py，然后就会报错。陷入悖论之中

解决：先注释掉views.py中的这一类查询，然后makemigrations，最后再恢复回来

## 1.3 非守护线程维持进程导致无法正确退出

和第一个问题类似，不过藏的更深，表现为执行makemigration后，命令未正常结束，而是卡在那里。

```python
views.py
class Handler():
    def __init__(self):
        xxxxx
        thread.Thread().start()
handler=Handler()
```


handler此时是个单例，所以Handler里面的__init__会被执行到。意味着如果__init__存在 thread.Thread().start()线程启动语句的话，那么也会被执行，创建出子线程。这会导致makemigrations结束后，无法自动退出，光标在最后一行输出后闪动（实际makemigrations以及成功完成），由于子线程有锁，会阻塞父进程的退出（父进程认为事情没干完，所以也阻塞在那里）。

这个问题迷惑性较强，一般第一反应都是models.py写的有问题。其实和models.py没关系。

本质原因是代码不规范导致的。__init__中是初始化部分，最好别包含线程启动等实际性执行操作。可以用start函数统一启动，这样也丰富编码规范。

## 1.4 django.db.utils.OperationalError: no such table.

```
python  manage.py  makemigrations  
python   manage.py  migrate 
``` 

数据库中有一个django_migrations数据表,找到你需要创建数据表的那个name,然后delete,再运行上面两个文件即可解决报错问题.




