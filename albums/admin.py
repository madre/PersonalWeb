#coding=utf-8
"""
__create_time__ = '13-10-13'
__author__ = 'Madre'
"""
from django.contrib import admin
from albums.models import Albums, Pictures, CATEGORY

from django.utils.safestring import mark_safe
from django.forms.widgets import FileInput


class AdminImageFieldWithThumbWidget(FileInput):
    def __init__(self, thumb_width=50, thumb_height=50):
        self.width = thumb_width
        self.height = thumb_height
        super(AdminImageFieldWithThumbWidget, self).__init__({})

    def render(self, name, value, attrs=None):
        thumb_html = ''
        if value and hasattr(value, "url"):
            thumb_html = '<img src="%s" width="%s" width="%s"/>' % (value.url, self.width, self.height)
        return mark_safe("%s%s" % (thumb_html,
                                   super(AdminImageFieldWithThumbWidget, self).render(name, value, attrs)))


class PhotoBaseInline(admin.TabularInline):
    model = Pictures

    fieldsets = (
        (u"图片", {'fields': (('title', 'thumbnail', 'index'),)}),
    )

    thumb_width = 150
    thumb_height = 150
    #
    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     field = super(PhotoBaseInline, self).formfield_for_dbfield(db_field, **kwargs)
    #     if db_field.name == 'thumbnail':
    #         return forms.ImageField(widget=AdminImageFieldWithThumbWidget(thumb_width=self.thumb_width,
    #                                                                       thumb_height=self.thumb_height))
    #     return field


# class AlbumsAdminForm(forms.ModelForm):
#     class Meta:
#         model = Albums
#
#     def __init__(self, *arg, **kwargs):
#         # 可以使用form预置或改写某字段的值
#         super(AlbumsAdminForm, self).__init__(*arg, **kwargs)
#         self.fields['category'].choices = [(csc.id, csc.name) for csc in CATEGORY.objects.filter(m_type='picture')]


class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'index')
    list_display_links = ['title']
    list_editable = ['index']
    date_hierarchy = 'createtime'
    list_filter = ['category', 'title']
    search_fields = ['title', 'description']
    inlines = [
        PhotoBaseInline,
    ]


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('albums', 'title', 'index', 'createtime', 'updatetime')
    list_display_links = ['title']
    list_editable = ['index']
    date_hierarchy = 'createtime'
    search_fields = ['title', ]


admin.site.register(Albums, AlbumsAdmin)
admin.site.register(Pictures, PicturesAdmin)
