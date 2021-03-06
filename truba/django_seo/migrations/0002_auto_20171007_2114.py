# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-07 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_seo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo_words',
            name='name',
            field=models.CharField(default=1, max_length=255, unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seo_words',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
