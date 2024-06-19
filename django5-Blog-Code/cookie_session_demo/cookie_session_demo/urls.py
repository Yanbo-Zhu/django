"""
URL configuration for cookie_session_demo project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookie/add', views.add_cookie, name='add cookie'),
    path('cookie/delete', views.delete_cookie, name='delete cookie'),
    path('cookie/get', views.get_cookie, name='get cookie'),
    path('session/add', views.add_session, name='add session'),
    path('session/get', views.get_session, name='get session')
]
