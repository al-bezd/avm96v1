#coding:utf8
import os

from django.core.serializers import json
from django.http.response import HttpResponseNotFound, HttpResponse

from chat_app.models import ChatConsultant
from django.shortcuts import render

from base_app.models import Catalog, Production, Specifications, Order,base_setting
from django_seo.models import SEO_Words
#from site_settings.models import Contacts,GrandOptions,GrandPage, SiteInfo


#import pytelegrambotapi
from truba.settings import BASE_DIR


def context_catalog():
    #context = {}
    context=base_setting()

    r=Production.objects.all().order_by('sum_orders')[0:6]
    context['catalog'] = Catalog.objects.all()
    context['recomended'] = r
    ### nastroyki bota
    try:
        context['chat_on']=ChatConsultant.objects.filter(status=True)[0].status
    except:
        context['chat_on']=False
    ###
    #context['grand_page']=GrandPage.objects.filter(on=True)

    return context

def grand(request):

    context = context_catalog()
    try:
        context['seo_title_page'] = SEO_Words.objects.get(alias='glavnaya-stranica')
    except:
        context['seo_title_page'] = ''

    #context['info']=SiteInfo.objects.all()
    #context['block_info']=context['info']
    response=render(request,'base_app/grand.html',context)
    return response

def choise_catalog(request,catalog_resp):
    context = context_catalog()

    try:
        context['seo_title_page'] = SEO_Words.objects.get(catalog__alias=catalog_resp)
    except:
        context['seo_title_page'] = ''
    context['catalog'] = Catalog.objects.all()
    try:
        context['catalog_in']=Catalog.objects.filter(parent_alias=Catalog.objects.get(alias=catalog_resp).parent_alias)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    p=Production.objects.filter(parent=Catalog.objects.get(alias=catalog_resp))
    context['production'] = p
    context['name_catalog']=Catalog.objects.get(alias=catalog_resp)
    context['title_page'] = context['name_catalog'].name
    try:
        p_catalog=Catalog.objects.get(alias=catalog_resp)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    context['production_catalog']=Catalog.objects.filter(parent_alias=catalog_resp)
    context['parent_href'] = p_catalog
    try:
        context['parent_href_over']=Catalog.objects.get(alias=p_catalog.parent_alias)
    except:
        pass

    response = render(request, 'base_app/catalog.html', context)
    return response

def choise_production(request,prod_resp):
    context = context_catalog()
    #context['seo_title_page'] = Production.objects.get(SEO_Words__alias=prod_resp).title
    try:
        context['seo_title_page'] = SEO_Words.objects.get(production__alias=prod_resp)
    except:
        context['seo_title_page'] = ''

    try:
        context['production']=Production.objects.get(alias=prod_resp)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    context['title_page'] = context['production'].name
    p=Production.objects.get(alias=prod_resp)
    p_catalog=Catalog.objects.get(name=p.parent)
    context['parent_href'] = Catalog.objects.get(name=Production.objects.get(alias=prod_resp).parent)
    context['parent_href_over']=Catalog.objects.get(alias=p_catalog.parent_alias)

    if request.method == 'POST':
        if request.POST.get('name_client'):
            p=Production.objects.get(alias=request.POST['alias'])
            order=Order(
                name_client=request.POST['name_client'],
                tel = request.POST['tel'],
                email = request.POST['email'],
                product = '%s|%s'%(p.name,p.alias),
                comment = request.POST['comment'],
            )
            order.save()
            p.sum_orders = +1
            p.save()
        if request.POST.get('views'):
            p=Production.objects.get(alias=request.POST['views'])
            p.views=p.views+1
            p.save()

    response = render(request, 'base_app/production.html', context)
    return response

def add_order(request):
    if request.method == 'POST':
        if request.POST.get('name_client'):
            p=Production.objects.get(alias=request.POST['alias'])
            order=Order(
                name_client=request.POST['name_client'],
                tel = request.POST['tel'],
                email = request.POST['email'],
                product = '%s|%s'%(p.name,p.alias),
                comment = request.POST['comment'],
            )
            order.save()
            p.sum_orders = +1
            p.save()
            return HttpResponse('Done!')

