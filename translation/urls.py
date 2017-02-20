# coding=utf-8
"""
__create_time__ = '13-10-16'
__author__ = 'Madre'
"""
from django.conf.urls import url

from .views import *

urlpatterns = (
    url(r'^(?P<pk>\d+)/$', TranslationDetailView.as_view(),
        name='translation_detail'),
    url(r'^$', TranslationListView.as_view(), name='translation_list'),
    url(r'^(?P<m_type>\w+)/$', TranslationListView.as_view(),
        name='translation'),
)
