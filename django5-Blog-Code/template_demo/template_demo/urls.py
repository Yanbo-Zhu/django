"""
URL configuration for template_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('baidu', views.baidu, name='baidu'),
    path('info', views.info, name='info'),
    path('if', views.if_view, name='if'),
    path('for', views.for_view, name='for'),
    path('with', views.with_view, name='with'),
    path('url', views.url_view, name='url'),
    path('book/<book_id>', views.book_detail, name='book_detail'),
    path('filter', views.filter_view, name='filter'),
    path('template/form', views.template_form, name='template_form'),
    path('sta', views.static_view, name='static_view')
]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
