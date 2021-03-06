#coding=utf-8
"""
__create_time__ = '13-10-29'
__author__ = 'Madre'
"""
from django.forms import ModelForm, CharField, Textarea
from brief.models import Brief


class BriefCreateForm(ModelForm):
    brief = CharField(max_length=1000, widget=Textarea(attrs={'cols': 2, 'rows': 2}))

    class Meta:
        model = Brief
        exclude = ('slug',)