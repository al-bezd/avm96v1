#coding:utf8
from __future__ import unicode_literals

import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPRecipientsRefused

import mptt
from ckeditor.fields import RichTextField
import simplejson as json
from django.db import models
# Create your models here.
###########################################################################################################
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from django_seo import models as seo_models
from truba.settings import BASE_DIR, DEV_EMAIL, DEBUG


class Catalog(MPTTModel):
    class Meta():
        verbose_name_plural = u'Категории'
        verbose_name = u'Категория'
        ordering = ('tree_id', 'level')


    name = models.CharField(max_length=255, verbose_name=u'Категория')
    alias = models.SlugField(verbose_name=u'Alias категории')
    parent_alias = models.SlugField(verbose_name=u'Alias Родителя',default='none')
    parent = TreeForeignKey('self', blank=True, null=True, related_name=u'children'
                            # , verbose_name='РОДИТЕЛЬСКИЙ класс'
                            )
    units_of_calculus = models.CharField(max_length=10, verbose_name='Единицы исчесления', blank=True, null=True,default=u'шт.')

    #child = models.CharField(max_length=255, verbose_name='Количество Детей', default=0, blank=True, null=True)
    img = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    #
    seo=models.ForeignKey(seo_models.SEO_Words)

    def __unicode__(self):
        return '%s' % (self.name)

    def save(self, *args,**kwargs):
        if self.parent:
            self.parent_alias=str(Catalog.objects.get(name=unicode(self.parent)).alias)
        super(Catalog, self).save()
    def prew_img(self):
        if self.img:
            return '<img src="%s" width="100">' % self.img.url
        else:
            return u'(Нет картинки)'
    prew_img.short_description = u'Изображение'
    prew_img.allow_tags = True






    class MPTTMeta:
        order_insertion_by = ['name']
mptt.register(Catalog, order_insertion_by=['name'])


#########################################################################################
class Specifications(models.Model):



    prod = models.CharField(max_length=255, verbose_name='Продукция')
    destiny = models.CharField(max_length=255, verbose_name='Предназначение', default=u'Для (предназначение)')
    product_description = RichTextField(verbose_name='Описание продукции', blank=True, null=True)
    application_area = RichTextField(verbose_name='Область применения', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена', blank=True, null=True)
    # units_of_calculus=models.CharField(max_length=10,verbose_name='Единицы исчесления')
    img = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    comment = RichTextField(blank=True, null=True, verbose_name='Комментарий')
    class Meta():
        verbose_name_plural = 'Спецификация'
        verbose_name = 'Спецификация'

    def __unicode__(self):
        return '%s'%(self.prod)
    def prew_img(self):
        if self.img:
            return '<img src="%s" width="100">' % self.img.url
        else:
            return u'(Нет картинки)'
    prew_img.short_description = u'Изображение'
    prew_img.allow_tags = True

class Production(models.Model):
    name=models.CharField(max_length=255, verbose_name='Название Продукта')
    title=models.CharField(max_length=255,verbose_name='Заголовок')

    specifications = models.ForeignKey(Specifications, verbose_name='Спецификация')
    alias=models.SlugField(verbose_name='Псевдоним')
    #price=models.DecimalField(max_digits=12,decimal_places=2,verbose_name='Цена')
    parent=models.ForeignKey(Catalog,verbose_name='Каталог')
    #img=models.ImageField(verbose_name='Изображение',blank=True,null=True)
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    #### novoe ot 14.08.2017
    sum_orders=models.IntegerField(default=0,verbose_name='Количество заказов')
    views=models.IntegerField(default=0,verbose_name='Просмотры')
    ########################
    seo = models.ForeignKey(seo_models.SEO_Words)
    #########################
    class Meta():
        verbose_name_plural = 'Продукция'
        verbose_name = 'Продукцию'



    def __unicode__(self):
        return '%s'%(self.name)
    def prew_img(self):
        if self.specifications.img:
            return '<img src="%s" width="100">' % self.specifications.img.url
        else:
            return u'(Нет картинки)'

    prew_img.short_description = u'Изображение'
    prew_img.allow_tags = True

class Order(models.Model):
    class Meta():
        verbose_name_plural = 'Заказы от клиентов'
        verbose_name = 'Заказы от клиентов'
    name_client=models.CharField(max_length=255,verbose_name=u'ФИО Клиента')
    tel=models.CharField(max_length=30,verbose_name=u'Контактный номер Клиента')
    email=models.EmailField(null=True,blank=True,verbose_name=u'Эл.почта')
    product=models.CharField(max_length=255,verbose_name=u'Продукт вызвавший интерес')
    date_create=models.DateTimeField(auto_now_add=True,verbose_name=u'Дата созданния')
    #time_create
    comment=models.TextField(blank=True,null=True,verbose_name=u'Сообщение')
    status=models.CharField(max_length=255,default=u'Не выполнен',verbose_name=u'Статус заказа')



    def __unicode__(self):
        return '%s'%(self.id)
    def prew_img(self):
        if Production.objects.get(alias=self.product).specifications.img.url:
            return '<img src="%s" width="75">' % Production.objects.get(alias=self.product).specifications.img.url
        else:
            return u'(Нет картинки)'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        p = self.product.split('|')[1]
        prod=Production.objects.get(alias=p).alias
        c=Order.objects.filter(product=self.product)
        g=Production.objects.get(alias=p)
        g.sum_orders=len(c)
        g.save()
        super(Order, self).save()
        c=base_setting()
        try:
            b = smtplib.SMTP(c['smtp'], c['port'])
            b.starttls()
            b.login(c['email_from'], c['password'])
            text = "<span>Заказ №%s</span><br>" \
                   "<span>ФИО - %s</span><br>" \
                   "<span>Телефон - %s</span><br>" \
                   "<span>Email - %s</span><br>" \
                   "<span>Продукт - %s</span><br>"%(self.id,self.name,self.tel,self.email,self.product)

            #msg = MIMEMultipart()
            msg = MIMEText(text, "html", "utf8")
            msg['From'] = c['email_from']
            msg['To'] = c['email_to']
            msg['Subject'] = unicode(u'Заказ сделан ').encode('utf8') + unicode(
                c.name).encode('utf8')
            if DEBUG:
                poluchatel = c['email_from']
            else:
                poluchatel = self.email
                #send to client
            b.sendmail(c['email_from'],
                       # request.POST['email'], #raskomentit' na prodaktion
                       poluchatel,
                       str(msg))
                #send to manager
            b.sendmail(c['email_from'],
                       c['email_to'],
                       str(msg))
            b.quit()
        except SMTPRecipientsRefused:
            print "Сообщение не отправленно 'SMTPRecipientsRefused'"
    prew_img.short_description = u'Изображение'
    prew_img.allow_tags = True

def base_setting():
    try:
        f=open('%s/setting.json'%(BASE_DIR),'r')
    except:
        f = open('%s/setting.json' % (BASE_DIR), 'w')
        f.close()
    f = open('%s/setting.json' % (BASE_DIR), 'r')
    set=f.read()
    f.close()
    if not set:
        content={
            'company': '',
            'logo': '',
            'tel': '',
            'email': '',
            'nation': '',
            'region': '',
            'city': '',
            'street': '',
            'home': '',
            'office': '',
            'seo_links': '',
            'yan_x': '',
            'yan_y': '',

        }
        content['smtp'] = ''
        content['port'] = ''
        content['email_from'] = ''
        content['password'] = ''
        content['email_to'] = ''
        with open("setting.json", "w") as file:
            json.dump(content, file)
    else:
        content=json.load(open('setting.json'))
    content['dev_email'] = DEV_EMAIL
    return content