# -*- coding: UTF-8 -*-
from chat_app.models import ChatConsultant
from django import template
from django.http import HttpResponseRedirect

register = template.Library()



@register.inclusion_tag(
'chat_app/base.html')  # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist
def chat_bot_tag():
    context={}
    consultant=ChatConsultant.objects.all().order_by('?')[0]



    context['consultant']=consultant
    #context['bot_on']=bot_on# можно передавать не только строки, но и сложные объекты типа выборки из базы данных
    return context
