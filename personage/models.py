#!/usr/bin/env python
# encoding: utf-8
# Date: 2020/12/07
# file: base_model.py
# Email:
# Author: 唐政

from django.db import models
from util.base_model import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=10, unique=True, verbose_name=u'用户名', help_text=u'用户名')
