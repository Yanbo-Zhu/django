

前面我们体验了Admin系统，以及模型注册，自定义设置。但是依然满足不了我们实际的业务开发
需求。接下来，我们来讲下更细致的Admin系统二次开发。

# 1 创建一个普通管理员账户
首先我们在Admin后台系统里新建一个普通管理员账号。
认证和授权的用户右侧点击“新增”

![[08_内置admin系统/images/Pasted image 20240619225550.png]]

![[08_内置admin系统/images/Pasted image 20240619225558.png]]


# 2 设置不可编辑字段 get_readonly_fields()

业务开发时，有时候一些敏感字段，我们不允许普通管理员修改。我们可以通过重写ModelAdmin的get_readonly_fields()方法实现；

```
# 重写分类方法，设置只读字段
def get_readonly_fields(self, request, obj=None):
	if request.user.is_superuser:
		self.readonly_fields = []
	else:
		self.readonly_fields = ['bookName']
	return self.readonly_fields
```


我们用普通管理员fengge登录，然后点击编辑，
![[08_内置admin系统/images/Pasted image 20240619225642.png]]

图书名称已经变成只读了。


这里我们同时也发现，字段label名称是英文BookName，原因是我们没有设置属性字段的 verbose_name
我们可以在models.py里，加下verbose_name配置即可；

![[08_内置admin系统/images/Pasted image 20240619225705.png]]

再进入下系统，
![[08_内置admin系统/images/Pasted image 20240619225742.png]]


用python222管理员登录的话，是所有字段都可以编辑的。

![[08_内置admin系统/images/Pasted image 20240619225801.png]]

当然还有很多细粒度设置的方法，如下
formfield_for_foreignkey() 设置外键下拉框过滤筛选
formfield_for_foreignkey() 重写外键下拉框数据，比如增加下拉选项。
save_model() 添加或者修改处理逻辑重写 ，可以增加一些日志等处理。
等等...

# 3 自定义Admin模版
Admin后台管理系统的模版文件和Django框架内置提供的，我们可以在源码里找到。
具体位置在django -> contrib -> admin -> templates 下

![[08_内置admin系统/images/Pasted image 20240619225828.png]]

很多时候我们需要修改默认的模版，包括程序功能，样式等，来达到业务需求。
我们可以直接修改源码里的模版，但是这种方式不好，如果一台机器有多个项目，会影响其他项目使用。
我们提倡在项目的模块项目的templates下，通过优先级来实现修改模版。

具体方式如下：
模块项目(比如我们这是helloWorld项目)的templates下，新建admin目录，然后admin目录下创建你需要覆盖的模版名称。
比如我们覆盖下修改的模版change_form.html。

![[08_内置admin系统/images/Pasted image 20240619225855.png]]

从django源码里复制一份源码，贴进去，然后根据需求我们改下。
我们先测试下

change_form.html官方模版源码是如下：
```html
{% extends "admin/base_site.html" %} {% load i18n admin_urls static admin_modify %} {% block extrahead %}{{ block.super }}
<script src="{% url 'admin:jsi18n' %}"></script>
{{ media }} {% endblock %} {% block extrastyle %}{{ block.super }}<link rel="stylesheet" href="{% static "admin/css/forms.css" %}">{% endblock %} {% block coltype %}colM{% endblock %} {% block bodyclass %}{{ block.super }} app-{{
opts.app_label }} model-{{ opts.model_name }} change-form{% endblock %} {% if not is_popup %} {% block breadcrumbs %}
<div class="breadcrumbs">
    <a href="{% url 'admin:index' %}">{% translate 'Home' %}</a>
    &rsaquo; <a href="{% url 'admin:app_list' app_label=opts.app_label %}">{{ opts.app_config.verbose_name }}</a> &rsaquo; {% if has_view_permission %}
    <a
        href="{% url
opts|admin_urlname:'changelist' %}"
    >
        {{ opts.verbose_name_plural|capfirst }}
    </a>
    {% else %}{{ opts.verbose_name_plural|capfirst }}{% endif %} &rsaquo; {% if add %}{% blocktranslate with name=opts.verbose_name %}Add {{ name }}{% endblocktranslate %}{% else %}{{ original|truncatewords:"18" }}{% endif %}
</div>
{% endblock %} {% endif %} {% block content %}
<div id="content-main">
    {% block object-tools %} {% if change and not is_popup %}
    <ul class="object-tools">
        {% block object-tools-items %} {% change_form_object_tools %} {% endblock %}
    </ul>
    {% endif %} {% endblock %}
    <form
        {%
        if
        has_file_field
        %}enctype="multipart/form-data"
        {%
        endif
        %}{%
        if
        form_url
        %}action="{{ form_url }}"
        {%
        endif
        %}method="post"
        id="{{
opts.model_name }}_form"
        novalidate
    >
        {% csrf_token %}{% block form_top %}{% endblock %}
        <div>
            {% if is_popup %}<input type="hidden" name="{{ is_popup_var }}" value="1" />{% endif %} {% if to_field %}
            <input
                type="hidden"
                name="{{ to_field_var }}"
                value="{{
to_field }}"
            />
            {% endif %} {% if save_on_top %}{% block submit_buttons_top %}{% submit_row %}{% endblock %}{% endif %} {% if errors %}
            <p class="errornote">
                {% blocktranslate count counter=errors|length %}Please correct the error below.{% plural %}Please correct the errors below.{% endblocktranslate %}
            </p>
            {{ adminform.form.non_field_errors }} {% endif %} {% block field_sets %} {% for fieldset in adminform %} {% include "admin/includes/fieldset.html" %} {% endfor %} {% endblock %} {% block after_field_sets %}{% endblock %} {%
            block inline_field_sets %} {% for inline_admin_formset in inline_admin_formsets %} {% include inline_admin_formset.opts.template %} {% endfor %} {% endblock %} {% block after_related_objects %}{% endblock %} {% block
            submit_buttons_bottom %}{% submit_row %}{% endblock %} {% block admin_change_form_document_ready %}
            <script id="django-admin-form-add-constants" src="{% static 'admin/js/change_form.js' %}" {% if adminform and add %} data-model-name="{{ opts.model_name }}" {% endif %} async></script>
            {% endblock %} {# JavaScript for prepopulated fields #} {% prepopulated_fields_js %}
        </div>
    </form>
</div>
{% endblock %}


```



运行效果如下：
![[08_内置admin系统/images/Pasted image 20240619230018.png]]



我们从测试有效性的出发点来删除源码，改造如下：
```html
{% extends "admin/base_site.html" %} 
{% load i18n admin_urls static admin_modify %} 

{% block extrahead %}{{ block.super }}
<script src="{% url 'admin:jsi18n' %}"></script>
	{{ media }} 
{% endblock %} 

{% block extrastyle %}{{ block.super }}
	<link rel="stylesheet" href="{% static "admin/css/forms.css" %}">{% endblock %} 
	
{% block coltype %}colM{% endblock %}
```

再刷新页面看下：


![[08_内置admin系统/images/Pasted image 20240619230157.png]]


