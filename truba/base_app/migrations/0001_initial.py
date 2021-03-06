# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-05 17:46
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_seo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('alias', models.SlugField(verbose_name='Alias \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
                ('parent_alias', models.SlugField(default='none', verbose_name='Alias \u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044f')),
                ('units_of_calculus', models.CharField(blank=True, default='\u0448\u0442.', max_length=10, null=True, verbose_name='\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0441\u0447\u0435\u0441\u043b\u0435\u043d\u0438\u044f')),
                ('img', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='base_app.Catalog')),
                ('seo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_seo.SEO_Words')),
            ],
            options={
                'ordering': ('tree_id', 'level'),
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_client', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e \u041a\u043b\u0438\u0435\u043d\u0442\u0430')),
                ('tel', models.CharField(max_length=30, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u041a\u043b\u0438\u0435\u043d\u0442\u0430')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='\u042d\u043b.\u043f\u043e\u0447\u0442\u0430')),
                ('product', models.CharField(max_length=255, verbose_name='\u041f\u0440\u043e\u0434\u0443\u043a\u0442 \u0432\u044b\u0437\u0432\u0430\u0432\u0448\u0438\u0439 \u0438\u043d\u0442\u0435\u0440\u0435\u0441')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u0438\u044f')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('status', models.CharField(default='\u041d\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d', max_length=255, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437\u044b \u043e\u0442 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b \u043e\u0442 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u041f\u0440\u043e\u0434\u0443\u043a\u0442\u0430')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('alias', models.SlugField(verbose_name='\u041f\u0441\u0435\u0432\u0434\u043e\u043d\u0438\u043c')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('sum_orders', models.IntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432')),
                ('views', models.IntegerField(default=0, verbose_name='\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u044b')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.Catalog', verbose_name='\u041a\u0430\u0442\u0430\u043b\u043e\u0433')),
                ('seo', models.ManyToManyField(to='django_seo.SEO_Words')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044e',
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod', models.CharField(max_length=255, verbose_name='\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f')),
                ('destiny', models.CharField(default='\u0414\u043b\u044f (\u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435)', max_length=255, verbose_name='\u041f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
                ('product_description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438')),
                ('application_area', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='\u0426\u0435\u043d\u0430')),
                ('img', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('comment', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
            ],
            options={
                'verbose_name': '\u0421\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f',
            },
        ),
        migrations.AddField(
            model_name='production',
            name='specifications',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.Specifications', verbose_name='\u0421\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f'),
        ),
    ]
