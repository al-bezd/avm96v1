# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-12 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0011_chatsetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatsetting',
            name='title',
            field=models.CharField(default=1, max_length=50, verbose_name='\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438'),
            preserve_default=False,
        ),
    ]
