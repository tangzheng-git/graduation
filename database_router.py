#!/usr/bin/env python
# encoding: utf-8
# Date: 2020/12/07
# file: database_router.py.py
# Email:
# Author: 唐政 


from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING


class DatabaseAppsRouter(object):
    """
    一个路由器，用于控制不同数据库模型上的所有数据库操作。
    如果应用程序没有在设置中设置。DATABASE_APPS_MAPPING，路由器将回退到“默认”数据库。

    Settings example:
    DATABASE_APPS_MAPPING = {
                            'app1': 'db1',
                            'app2': 'db2'
    }
    """

    @staticmethod
    def db_for_read(model, **hints):
        """"
        将所有读取操作指向特定的数据库。
        """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    @staticmethod
    def db_for_write(model, **hints):
        """
        将所有写操作指向特定的数据库。
        """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    @staticmethod
    def allow_relation(obj1, obj2, **hints):
        """
        允许使用相同数据库的应用程序之间存在任何关系。
        """
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    # for Django 1.4 - Django 1.6
    @staticmethod
    def allow_syncdb(db, model):
        """
        确保应用程序只出现在相关数据库中。
        """

        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(model._meta.app_label) == db
        elif model._meta.app_label in DATABASE_MAPPING:
            return False
        return None

    # Django 1.7 - Django 1.11
    @staticmethod
    def allow_migrate(db, app_label, model_name=None, **hints):
        print(db, app_label, model_name, hints)
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(app_label) == db
        elif app_label in DATABASE_MAPPING:
            return False
        return None