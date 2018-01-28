#coding:utf8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class SEO_Words(models.Model):
    class Meta():
        verbose_name_plural = 'seo'
        verbose_name = 'seo'

    name = models.CharField(max_length=255, verbose_name=u'Название', unique=True)
    alias=models.SlugField(verbose_name=u'Псевдоним',blank=True,null=True)
    title=models.CharField(max_length=255,verbose_name=u'Заголовок')
    words=models.TextField(verbose_name=u'Ключевые слова',blank=True,null=True)
    alt=models.TextField(verbose_name=u'Краткое описание',blank=True,null=True)

    def __unicode__(self):
        return ('%s')%(self.name)
try:
    s=SEO_Words(name=u'Главная страница',title=u'Название организации|описание рода деятельности',words='key words')
    s.save()
except:
    pass
