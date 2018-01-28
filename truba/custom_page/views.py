# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from base_app.models import base_setting
import simplejson as json
from truba.settings import MEDIA_URL, DEV_EMAIL

context={}
def show_admin_custom_page(request):
    context=base_setting()
    if request.POST.get('save'):
        context['company']=request.POST.get('company')
        context['logo'] =request.POST.get('logo')
        context['tel'] =request.POST.get('tel')
        context['email'] =request.POST.get('email')
        context['nation'] =request.POST.get('nation')
        context['region'] =request.POST.get('region')
        context['city'] =request.POST.get('city')
        context['street'] =request.POST.get('street')
        context['home'] =request.POST.get('home')
        context['office'] =request.POST.get('office')
        context['seo_links'] =request.POST.get('seo_links')
        context['yan_x'] =request.POST.get('yan_x')
        context['yan_y'] =request.POST.get('yan_y')

        context['smtp'] =request.POST.get('smtp')
        context['port'] =request.POST.get('port')
        context['email_from'] =request.POST.get('email_from')
        context['password'] =request.POST.get('password')
        context['email_to'] =request.POST.get('email_to')

    with open("setting.json", "w") as file:
        json.dump(context, file)


    return render(request, 'custom_page/admin_custom_page.html', context)