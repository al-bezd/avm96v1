from django.contrib import admin
from models import *
# Register your models here.
@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = (
        'id_room',
        'date_create',
    )
    list_display_links = (
        'id_room',
        'date_create',
    )

@admin.register(ChatConsultant)
class ChatConsultantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'prew_img',
        'rang',
        'status'
    )
    list_display_links = (
        'name',
        'rang',
    )
    list_editable = ['status']

'''@admin.register(ChatSetting)
class ChatSettingAdmin(admin.ModelAdmin):


    def has_delete_permission(self, request,obj=None):
        return False
    pass
'''



