"""truba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from base_app.urls import urlpatterns as urlpatterns_base_app
from chat_app.urls import urlpatterns as urlpatterns_chat_app
#from tinymce.urls import urlpatterns as urlpatterns_tinymce
from questions.urls import urlpatterns as urlpatterns_quest

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_messages.urls import urlpatterns as urlpatterns_django_messages
import settings
urlpatterns=[]
urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('custom_page.urls')),
    #url(r'^ckeditor/', include('ckeditor.urls')),
]+urlpatterns_chat_app+urlpatterns_quest
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += urlpatterns_base_app
