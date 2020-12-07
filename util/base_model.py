#!/usr/bin/env python
# encoding: utf-8
# Date: 2020/12/07
# file: base_model.py
# Email:
# Author: 唐政


from django.utils import timezone
from django.db import models


class BaseModel(models.Model):
    """
    基础Model类
    """

    is_active = models.BooleanField(default=True, verbose_name=u'状态')
    create_time = models.DateTimeField(default=timezone.now, db_index=True, verbose_name=u'创建时间')

    def __unicode__(self):
        if hasattr(self, 'name'):
            # <model pk: name>
            return u'<{} {}: {} >'.format(self.__class__.__name__, self.pk, self.name)
        else:
            raise Exception(u'需要重载 __unicode__ 函数')

    def __repr__(self):
        return u'< {} {} >'.format(self.pk, type(self))

    def __str__(self):
        return u'< {} {} >'.format(self.pk, type(self))
