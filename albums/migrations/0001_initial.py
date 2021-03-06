# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='标题')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='albums', verbose_name='封面')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.CATEGORY')),
            ],
            options={
                'verbose_name': '相册',
                'verbose_name_plural': '相册',
                'ordering': ['-createtime'],
            },
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='图片')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('albums', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Albums')),
            ],
            options={
                'verbose_name': '图片',
                'verbose_name_plural': '图片',
                'ordering': ['-createtime'],
            },
        ),
    ]
