#coding:utf8
from __future__ import unicode_literals

from django.db import models
import simplejson as json
from truba.settings import BASE_DIR, DEV_EMAIL


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