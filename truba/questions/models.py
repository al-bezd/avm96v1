#coding:utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Questions(models.Model):
    class Meta():
        verbose_name_plural = 'Вопросы от посетителей'
        verbose_name = 'Вопросы от посетителей'

    name=models.CharField(max_length=255,verbose_name=u'ФИО')
    email=models.EmailField(blank=True,null=True,verbose_name=u'email')
    quest=models.TextField(blank=True,null=True,verbose_name=u'Вопрос')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата созданния')

    def __unicode__(self):
        return '%s|%s|%s' % (self.id, self.date_create, self.quest[0:10])
