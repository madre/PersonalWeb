# coding=utf-8
"""
__create_time__ = '13-10-18'
__author__ = 'Madre'
"""
from django.conf.urls import url

from .views import *

urlpatterns = (
    url(r'^(?P<pk>\d+)/$', ResourceDetailView.as_view(), name='resource_detail'),
    url(r'^$', ResourceListView.as_view(), name='resource_list'),
    url(r'^docs/$', DocsResourceView.as_view(), name='resource_docs'),
    url(r'^all/$', ResourceListView.as_view(), name='resource_all'),
    url(r'^topic/(?P<pk>\d+)/$', TopicDetailView.as_view(), name='topic_detail'),
    url(r'^topic/(?P<slug>[-\w]+)/$', TopicDetailView.as_view(), name='topic_slug'),
)
