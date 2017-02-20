#coding=utf-8
"""
__create_time__ = '13-10-13'
__author__ = 'Madre'
"""
from django.contrib import admin
from blog.models import CATEGORY, Blog, Tag


class CATEGORYAdmin(admin.ModelAdmin):
    list_display = ('name', 'help_text', 'm_type', )
    list_display_links = ['name']
    list_editable = ['m_type']
    list_filter = ['name']


class BlogAdmin(admin.ModelAdmin):
    # form = BlogAdminForm
    list_display = ('category', 'title', 'user', 'index', 'show')
    list_display_links = ['title']
    list_editable = ['show', 'index']
    date_hierarchy = 'createtime'
    list_filter = ['show', 'title']
    search_fields = ['title', 'content']


class BriefAdmin(admin.ModelAdmin):
    list_display = ('brief', 'user', 'createtime', 'updatetime')
    list_display_links = ['brief']
    date_hierarchy = 'createtime'
    search_fields = ['brief', ]


admin.site.register(CATEGORY, CATEGORYAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
