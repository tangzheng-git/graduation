#!/usr/bin/env python
# encoding: utf-8
# Date: 2020/12/07
# file: urls.py
# Email:
# Author: 唐政 

from django.urls import re_path
from personage import views


urlpatterns = [
    re_path('^home$', views.home),
]