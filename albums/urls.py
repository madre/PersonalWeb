# coding=utf-8
"""
__create_time__ = '13-10-13'
__author__ = 'Madre'
"""
from django.conf.urls import url
from django.views.generic import TemplateView

from .views import *

urlpatterns = (
    url(r'^(?P<slug>[-\w]+)/list/$', AlbumsListView.as_view(),
        name="albums_list"),
    url(r'^(?P<pk>\d+)/detail/$', AlbumsDetailView.as_view(),
        name="albums_detail"),
    url(r'^cute/$', TemplateView.as_view(template_name="pic_detail.html"),
        name="cute"),
    url(r'^source_code/$', TemplateView.as_view(template_name="furture.html"),
        name="source_code"),
)
