#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '4/22/16'
__author__ = 'deling.ma'
"""
import multiprocessing

bind = '0.0.0.0:5210'
max_requests = 1000
keepalive = 5

proc_name = 'personal'

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gaiohttp'

loglevel = 'info'
errorlog = '-'

x_forwarded_for_header = 'X-FORWARDED-FOR'
