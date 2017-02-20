# coding=utf-8
"""
__create_time__ = '13-10-16'
__author__ = 'Madre'
"""
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

TRANSLATION_CLASS = (
    ('en', '中英译'),
    ('ja', '中日译'),
)

POSITION_CHOICES = ['sidepanel', 'home']


class Translation(models.Model):
    m_type = models.CharField('翻译类别', max_length=36, choices=TRANSLATION_CLASS)
    slug = models.SlugField('slug', max_length=255, blank=True, default='')
    thumbnail = models.ImageField('配图', upload_to='blog', null=True, blank=True)
    title = models.CharField('原文标题', max_length=255, unique=True)
    origin_content = models.TextField('原文')
    tran_title = models.CharField('译文标题', max_length=255, unique=True)
    tran_content = models.TextField('译文')
    o_t_content = models.TextField('参照')
    position = models.CharField('位置', max_length=36,
                                choices=zip(POSITION_CHOICES, POSITION_CHOICES))
    index = models.IntegerField('排序', default=0)
    show = models.BooleanField('是否显示', default=True)
    user = models.ForeignKey(User)
    createtime = models.DateTimeField(auto_now_add=True, editable=False)
    updatetime = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Translation, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-createtime', ]
        verbose_name = "翻译"
        verbose_name_plural = "翻译"
