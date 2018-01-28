#coding:utf8
'''from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Setting(models.Model):
    name=models.CharField(max_length=255,default='name')
    logo=models.ImageField(null=True, blank=True, default='static/img/kassa1.png')
    def __unicode__(self):
        return self.id
class SettingContact(models.Model):
    tel_support=models.CharField(max_length=255,default='',null=True, blank=True)
    email_support=models.CharField(max_length=255,default='',null=True, blank=True)
    nation=models.CharField(max_length=255,default='',null=True, blank=True)
    city=models.CharField(max_length=255,default='',null=True, blank=True)
    street=models.CharField(max_length=255,default='',null=True, blank=True)
    home=models.CharField(max_length=255,default='',null=True, blank=True)
    def __unicode__(self):
        return self.id
class SettingSendEmail(models.Model):
    smtp=models.CharField(max_length=255, default='smtp.gmail.com',null=True, blank=True)
    port=models.IntegerField(default=587,null=True)
    email_from=models.CharField(max_length=255,verbose_name=u'От кого(email)',null=True, blank=True)
    password=models.CharField(max_length=90,default='password')
    email_to=models.CharField(max_length=255,verbose_name=u'Кому(email)',null=True, blank=True)
    def __unicode__(self):
        return self.id
class SettingYaMap(models.Model):
    x=models.CharField(max_length=150,null=True, blank=True)
    y=models.CharField(max_length=150,null=True, blank=True)
    def __unicode__(self):
        return self.id
try:
    Setting.objects.get(id=1)
except:
    s=Setting(id=1)
    s.save()
try:
    SettingContact.objects.get(id=1)
except:
    sc=SettingContact(id=1)
    sc.save()
try:
    SettingSendEmail.objects.get(id=1)

except:
    sse=SettingSendEmail(id=1)
    sse.save
try:
    SettingYaMap.objects.get(id=1)
except:
    sse=SettingYaMap(id=1)
    sse.save'''
