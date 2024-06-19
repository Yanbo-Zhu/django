from django.urls import path
from . import views

urlpatterns = [
    path('avg', views.avg_view, name='avg_view'),
    path('count', views.count_view, name='count_view'),
    path('maxmin', views.max_min_view, name='maxmin_view'),
    path('sum', views.sum_view, name='sum_view'),
    path('f', views.f_view, name='f_view'),
    path('q', views.q_view, name='q_view'),
]
