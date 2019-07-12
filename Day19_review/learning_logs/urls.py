"""Defines url patterns for learning_logs."""

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page.
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),

    # 显示所有的主题
    # url(r'^topics/$', views.topics, name='topics'),
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # # Show all topics.
    # url(r'^topics/$', views.topics, name='topics'),
    #
    # # Detail page for a single topic.
    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
