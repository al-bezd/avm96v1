from django.contrib import admin
from models import SEO_Words
@admin.register(SEO_Words)
class SEO_WordsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"alias": ("name",),}
    #list_display_links = ('title')
    list_display = ['name']
    pass
# Register your models here.
