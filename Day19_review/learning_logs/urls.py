"""Defines url patterns for learning_logs."""

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

    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),

    # 用于添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # # Show all topics.
    # url(r'^topics/$', views.topics, name='topics'),
    #
    # # Detail page for a single topic.
    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
