#coding:utf8
from __future__ import unicode_literals
from django.contrib import admin
from models import Questions
class Questions_Admin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'date_create',
        
    )
    list_display_links = (
        'name',
        'email',
        'date_create',

    )
admin.site.register(Questions, Questions_Admin)

# Register your models here.
