# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-08 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_seo', '0002_auto_20171007_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo_words',
            name='alias',
            field=models.SlugField(blank=True, null=True, verbose_name='\u041f\u0441\u0435\u0432\u0434\u043e\u043d\u0438\u043c'),
        ),
    ]
