
我们通常做查询操作的时候，都是通过模型名字.objects 的方式进行操作。其实模型名字.objects 是一个django.db.models.manager.Manager 对象，而Manager 这个类是一个“空壳”的类，他本身是没有任何的属性和方法的。他的方法全部都是通过Python 动态添加的方式，从QuerySet 类中拷贝过来的

![](images/Pasted%20image%2020240617164925.png)

所以我们如果想要学习ORM 模型的查找操作，必须首先要学会QuerySet 上的一些API 的使用。


# 1 返回新的QuerySet的方法

在使用QuerySet 进行查找操作的时候，可以提供多种操作。比如过滤完后还要根据某个字段进行排序， 那么这一系列的操作我们可以通过一个非常流畅的链式调用的方式进行。比如要从文章表中获取标题为 123 ，并且提取后要将结果根据发布的时间进行排序，那么可以使用以下方式来完成

`articles = Article.objects.filter(title='123').order_by('create_time')`

可以看到order_by 方法是直接在filter 执行后调用的。这说明filter 返回的对象是一个拥有 order_by 方法的对象。而这个对象正是一个新的QuerySet 对象。因此可以使用order_by 方法


# 2 常用的QuerySet方法

那么以下将介绍在那些会返回新的QuerySet 对象的方法。

1 filter 
将满足条件的数据提取出来，返回一个新的QuerySet 。具体的filter 可以提供什么条件查询。请见查询操作章节。

2 exclude
排除满足条件的数据，返回一个新的QuerySet 。示例代码如下：
`Article.objects.exclude(title__contains='hello')`
以上代码的意思是提取那些标题不包含hello 的图书。


3 annotate
给QuerySet 中的每个对象都添加一个使用查询表达式（聚合函数、F表达式、Q表达式、Func表达式等）的新字段

`articles = Article.objects.annotate(author_name=F("author__name"))`

以上代码将在每个对象中都添加一个author__name 的字段，用来显示这个文章的作者的年龄。


4 order_by
order_by ：指定将查询的结果根据某个字段进行排序。如果要倒叙排序，那么可以在这个字段的前面加一个负号


```
# 根据创建的时间正序排序
articles = Article.objects.order_by("create_time")

# 根据创建的时间倒序排序
articles = Article.objects.order_by("-create_time")

# 根据作者的名字进行排序
articles = Article.objects.order_by("author__name")

# 首先根据创建的时间进行排序，如果时间相同，则根据作者的名字进行排序
articles = Article.objects.order_by("create_time",'author__name')
```

一定要注意的一点是，多个order_by ，会把前面排序的规则给打乱，而使用后面的排序方式。比如以下代码：

`articles = Article.objects.order_by("create_time").order_by("author__name")`

他会根据作者的名字进行排序，而不是使用文章的创建时间。


5 values 
用来指定在提取数据出来，需要提取哪些字段。默认情况下会把表中所有的字段全部都提取出来，可以使用values 来进行指定，并且使用了values 方法后，提取出的QuerySet 中的数据类型不是模型，而是在values 方法中指定的字段和值形成的`字典`

```
articles = Article.objects.values("title",'content')
for article in articles:
    print(article)

```


以上打印出来的article 是类似于{"title":"abc","content":"xxx"} 的形式。
如果在values 中没有传递任何参数，那么将会返回这个恶模型中所有的属性。



6 values_list
类似于values 。只不过返回的QuerySet 中，存储的不是字典，而是`元组`。示例
代码如下
```
articles = Article.objects.values_list("id","title")
print(articles)
```

那么在打印articles 后，结果为`<QuerySet [(1,'abc'),(2,'xxx'),...]> `等。
如果在values_list 中只有一个字段。那么你可以传递flat=True 来将结果扁平化。

```
articles1 = Article.objects.values_list("title")
>> <QuerySet [("abc",),("xxx",),...]>

articles2 = Article.objects.values_list("title",flat=True)
>> <QuerySet ["abc",'xxx',...]>
```


7 all 
获取这个ORM 模型的QuerySet 对象


8 select_related 
在提取某个模型的数据的同时，也提前将相关联的数据提取出来。比如提取文章数据，可以使用select_related 将author 信息提取出来，以后再次使用article.author 的时候就不需要再次去访问数据库了。可以减少数据库查询的次数。

```
article = Article.objects.get(pk=1)
>> article.author # 重新执行一次查询语句

article = Article.objects.select_related("author").get(pk=2)
>> article.author # 不需要重新执行查询语句了
```

select_related 只能用在一对多或者一对一中，不能用在多对多或者多对一中。比如可以提前获取文章的作者，但是不能通过作者获取他的文章，或者是通过某篇文章获取这个文章所有的标签。


9
prefetch_related ：
这个方法和select_related 非常的类似，就是在访问多个表中的数据的时候，减少查询的次数。这个方法是为了解决多对一和多对多的关系的查询问题。比如要获取标题中带有hello 字符串的文章以及他的所有标签，

```
from django.db import connection
articles =
Article.objects.prefetch_related("tag_set").filter(title__contains='hello')

print(articles.query) # 通过这条命令查看在底层的SQL语句

for article in articles:
print("title:",article.title)
    print(article.tag_set.all())

# 通过以下代码可以看出以上代码执行的sql语句
for sql in connection.queries:
    print(sql)
```


但是如果在使用article.tag_set 的时候，如果又创建了一个新的QuerySet 那么会把之前的SQL优化给破坏

```
tags = Tag.obejcts.prefetch_related("articles")
for tag in tags:
    articles = tag.articles.filter(title__contains='hello') #因为filter方法会
重新生成一个QuerySet，因此会破坏掉之前的sql优化

# 通过以下代码，我们可以看到在使用了filter的，他的sql查询会更多，而没有使用filter的，只
有两次sql查询
for sql in connection.queries:
print(sql)
```



10 defer 
在一些表中，可能存在很多的字段，但是一些字段的数据量可能是比较庞大的，而此时你又不需要，比如我们在获取文章列表的时候，文章的内容我们是不需要的，因此这时候我们就可以使用defer 来过滤掉一些字段。这个字段跟values 有点类似，只不过defer 返回的不是字典，而是模型


```
articles = list(Article.objects.defer("title"))
for sql in connection.queries:
    print('='*30)
    print(sql)
```

在看以上代码的sql 语句，你就可以看到，查找文章的字段，除了title ，其他字段都查找出来了。当然，你也可以使用article.title 来获取这个文章的标题，但是会重新执行一个查询的语句

```
articles = list(Article.objects.defer("title"))
for article in articles:
    # 因为在上面提取的时候过滤了title
    # 这个地方重新获取title，将重新向数据库中进行一次查找操作
    print(article.title)
    
for sql in connection.queries:
    print('='*30)
    print(sql)
```


defer 虽然能过滤字段，但是有些字段是不能过滤的，比如id ，即使你过滤了，也会提取出来。

11 
only ：跟defer 类似，只不过defer 是过滤掉指定的字段，而only 是只提取指定的字段。


12 
get ：获取满足条件的数据。这个函数只能返回一条数据，并且如果给的条件有多条数据，那么这个方法会抛出MultipleObjectsReturned 错误，如果给的条件没有任何数据，那么就会抛出DoesNotExit 错误。所以这个方法在获取数据的只能，只能有且只有一条。

13 create ：
创建一条数据，并且保存到数据库中。这个方法相当于先用指定的模型创建一个对象，然后再调用这个对象的save 方法

```
article = Article(title='abc')
article.save()

# 下面这行代码相当于以上两行代码
article = Article.objects.create(title='abc')
```

14 get_or_create
根据某个条件进行查找，如果找到了那么就返回这条数据，如果没有查找到，那么就创建一个

```
obj,created= Category.objects.get_or_create(title='默认分类')
```

如果有标题等于默认分类的分类，那么就会查找出来，如果没有，则会创建并且存储到数据库中。

这个方法的返回值是一个元组，元组的第一个参数obj 是这个对象，第二个参数created 代表是否创建的


15 bulk_create
一次性创建多个数据
```
Tag.objects.bulk_create([
    Tag(name='111'),
    Tag(name='222'),
])
```

16 count 
获取提取的数据的个数。如果想要知道总共有多少条数据，那么建议使用count ，而不是使用len(articles) 这种。因为count 在底层是使用select count(*) 来实现的，这种方式比使用len 函数更加的高效。

17 first 和last 
返回QuerySet 中的第一条和最后一条数据。

18 aggregate 
使用聚合函数。

19 exists ：
判断某个条件的数据是否存在。如果要判断某个条件的元素是否存在，那么建议使用
exists ，这比使用count 或者直接判断QuerySet 更有效得多

```
if Article.objects.filter(title__contains='hello').exists():
    print(True)
    
比使用count更高效：
if Article.objects.filter(title__contains='hello').count() > 0:
    print(True)
也比直接判断QuerySet更高效：
if Article.objects.filter(title__contains='hello'):
    print(True)
```


20 distinct

去除掉那些重复的数据。这个方法如果底层数据库用的是MySQL ，那么不能传递任何的参数。比如想要提取所有销售的价格超过80元的图书，并且删掉那些重复的，那么可以使用 distinct 来帮我们实现，

```
books = Book.objects.filter(bookorder__price__gte=80).distinct()
```


需要注意的是，如果在distinct 之前使用了order_by ，那么因为order_by 会提取order_by 中指定的字段，因此再使用distinct 就会根据多个字段来进行唯一化，所以就不会把那些重复的数据删掉

```
orders =
BookOrder.objects.order_by("create_time").values("book_id").distinct()
```

那么以上代码因为使用了order_by ，即使使用了distinct ，也会把重复的book_id 提取出来。


21  update ：
执行更新操作，在SQL 底层走的也是update 命令。比如要将所有category 为空的 article 的article 字段都更新为默认的分类

`Article.objects.filter(category__isnull=True).update(category_id=3)`

注意这个方法走的是更新的逻辑。所以更新完成后保存到数据库中不会执行save 方法，因此不会更新auto_now 设置的字段


22 delete ：
删除所有满足条件的数据。删除数据的时候，要注意on_delete 指定的处理方式。

23 切片操作：有时候我们查找数据，有可能只需要其中的一部分。那么这时候可以使用切片操作来帮
我们完成。QuerySet 使用切片操作就跟列表使用切片操作是一样的

```
books = Book.objects.all()[1:3]
for book in books:
    print(book)
```

切片操作并不是把所有数据从数据库中提取出来再做切片操作。而是在数据库层面使用LIMIE 和 OFFSET 来帮我们完成。所以如果只需要取其中一部分的数据的时候，建议大家使用切片操作。

# 3 什么时候Django会将QuerySet转换为SQL去执 行


生成一个QuerySet 对象并不会马上转换为SQL 语句去执行。
比如我们获取Book 表下所有的图书：

```
books = Book.objects.all()
print(connection.queries)
```


我们可以看到在打印connection.quries 的时候打印的是一个空的列表。说明上面的QuerySet 并没有 真正的执行。
在以下情况下QuerySet 会被转换为SQL 语句执行：
1. 迭代：在遍历QuerySet 对象的时候，会首先先执行这个SQL 语句，然后再把这个结果返回进行迭代。比如以下代码就会转换为SQL 语句：
```
for book in Book.objects.all():
    print(book)
```


1. 使用步长做切片操作： QuerySet 可以类似于列表一样做切片操作。做切片操作本身不会执行SQL语句，但是如果如果在做切片操作的时候提供了步长，那么就会立马执行SQL 语句。需要注意的是，做切片后不能再执行filter 方法，否则会报错。
2. 调用len 函数：调用len 函数用来获取QuerySet 中总共有多少条数据也会执行SQL 语句。
3. 调用list 函数：调用list 函数用来将一个QuerySet 对象转换为list 对象也会立马执行SQL 语句。
4. 判断：如果对某个QuerySet 进行判断，也会立马执行SQL 语句。




