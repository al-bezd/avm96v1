#coding:utf8
from __future__ import unicode_literals

from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    name = 'base_app'
    verbose_name='Главное приложение'
