from django.contrib import admin
from models import Catalog, Production, Specifications, Order


# Register your models here.
class Cataog_Admin(admin.ModelAdmin):
    prepopulated_fields = {"alias": ("name",),"parent_alias": ("parent",)}

    list_display = (
        'prew_img',
        'name',
        'alias',
        'parent_alias',
        'parent',
        #'child',
    )
    '''list_display_links = (
        'name',
        'alias',
        'parent_alias',
        'parent',
        'child',
    )'''
    list_editable=(
        #'name',

        'alias',
        'parent_alias',
        'parent',
        #'child',
    )
class Production__Admin(admin.ModelAdmin):
    prepopulated_fields = {"alias": ("name",),}
    list_display = (

        'name',
        'alias','prew_img',
        #'price',
        'parent',
        'sum_orders',
        'views'
    )
    list_display_links = (
        'name',
        'alias',
        #'price',
        'parent',

    )
    exclude = ('sum_orders','views')
class Specifications__Admin(admin.ModelAdmin):
    #prepopulated_fields = {"alias": ("name",),}
    list_display = (
        'prew_img',
        'id',
        'prod',
        'price',

    )
    list_display_links = (
        'id',
        'prod',
        'price',


    )
class Order_Admin(admin.ModelAdmin):
    list_display = (
        'name_client',
        'tel',
        'prew_img',
        'product',
        'date_create',
        'status'
    )
    list_display_links = (
        'name_client',
        'tel',
        'product',
        'date_create',
    )

admin.site.register(Catalog, Cataog_Admin)
admin.site.register(Production, Production__Admin)
admin.site.register(Specifications, Specifications__Admin)
admin.site.register(Order, Order_Admin)