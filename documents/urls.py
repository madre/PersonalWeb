# coding=utf-8
"""
__create_time__ = '14-05-03'
__author__ = 'Madre'
"""
from django.conf.urls import url

from .views import HtmlTemplateView

urlpatterns = (
    url(r'^(?P<docs_name>\w+)/$', HtmlTemplateView.as_view(), name="html_docs"),
)
