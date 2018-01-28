    import os, sys
    sys.path.append('/home/admin_avm96/XXX')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'truba.settings'
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
