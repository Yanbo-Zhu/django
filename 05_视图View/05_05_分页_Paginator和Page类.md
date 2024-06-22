

Paginator 和Page 类都是用来做分页的。

在Django 中实现分页功能非常简单。因为Django 已经内置了两个处理分类的类。分别是Paginator 和Page 。Paginator 用来管理整个分类的一些属性， Page 用来管理当前这个分页的一些属性。通过这两
个类，就可以轻松的实现分页效果。以下对这两个类进行讲解。


他们在Django 中的路径为django.core.paginator.Paginator 和django.core.paginator.Page 。以下对这两个类的常用属性和方法做解释


# 1 Paginator类

Paginator 是用来控制整个分页的逻辑的。比如总共有多少页，页码区间等等。都可以从他上面来获取。

## 1.1 创建Paginator对象
class Paginator(object_list, per_page, orphans=0, allow_empty_first_page=True) ，其中的参数解释如下：
1. object_list ：列表，元组， QuerySet 或者是任何可以做切片操作的对象。会将这个里面的对象进行分页。
2. per_page ：分页中，一页展示多少条数据。
3. orphans ：用来控制最后一页元素的个人如果少于orphans 指定的个数的时候，就会将多余的添加到上一页中。
4. allow_empty_first_page ：如果object_list 没有任何数据，并且这个参数设置为True ，那么就会抛出EmptyPage 异常。

## 1.2 Paginator常用属性和方法：
1. Paginator.page(number) ：获取number 这页的Page 对象。
2. count ：传进来的objec_list 总共有多少条数据。
3. num_pages ：总共有多少页。
4. page_range ：页面的区间。比如有三页，那么就range(1,4) 。


## 1.3 例子 

最后我们列下 Paginator 常用属性结束 django 的入门教程
``````python
from django.core.paginator import Paginator
item_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# 指定 paginator 的列表以及每页显示的列表数量
p = Paginator(item_list, 2)
print(p.count) # 返回列表的总数	14
print(p.num_pages) # 返回总页数    7
print(p.page_range) # 返回页数的范围	(1, 8)
print(p.per_page) # 返回每页列表的数量
print(p.object_list) # 返回所有的列表 item

# 通过 page(num) 方法获取 num 页的列表 <Page 2 of 7>
page2 = p.page(2)
print(page2.number) # 获取当前页的页码
print(page2.object_list) # 获取该页码下的所有列表    ['c', 'd']
print(page2.has_next()) # 是否有下页    True
print(page2.has_previous()) # 是否有上页    True
print(page2.has_other_pages()) # 是否有其他页    True
# 如果没有上/下一页则返回 EmptyPage 错误 EmptyPage: That page contains no results
print(page2.next_page_number()) # 获取下一页的页码    3
print(page2.previous_page_number()) # 获取上一页的页码    1
print(page2.start_index()) # 当前页第一个 item 在列表中的位置    3
print(page2.end_index()) # 当前页最后一个 item 在列表中的位置    4
``````

# 2 page

Page常用属性和方法：
1. has_next ：是否还有下一页。
2. has_previous ：是否还有上一页。
3. next_page_number ：下一页的页码。
4. previous_page_number ：上一页的页码。
5. number ：当前页。
6. start_index ：当前这一页的第一条数据的索引值。
7. end_index ：当前这一页的最后一条数据的索引值。
