from django.urls import path
from . import views

app_name = 'zlauth'

urlpatterns = [
    path('login', views.zllogin, name='login'),
    path('logout', views.zllogout, name='logout'),
    path('register', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='email_captcha')
]