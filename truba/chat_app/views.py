from random import random, randint
from uuid import UUID

from django.shortcuts import render
from models import  *
from truba.settings import ID_ROOM
# Create your views here.
context={}

def chat(request):

    if request.method == 'POST':
        if request.POST.get('comment'):
            m=ChatRoom(#message=request.POST['messages'],
                       #wayanswer=request.POST['answerway'],
                       comment=request.POST['comment'],
                       id_room=request.POST['id_room'],)
            m.update_chat_room()

    response=render(request,'chat_app\\base.html',context)
    return response