#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: 橘子
# @Date  : 2020/9/28
# @Desc  : execise

from django.conf.urls import url
from . import views
urlpatterns = [
    url('^$', views.index_view),
    url(r'^index/', views.index2_view),

]