from django.shortcuts import render
from models import Questions

# Create your views here.
context={}
def quest(request):
    if request.method == 'POST':
        if request.POST.get('client_name'):
            quesst = Questions(
                name=request.POST['client_name'],
                email=request.POST['email'],
                quest=request.POST['question'],
            )
            quesst.save()
    response=render(request,'base_app/catalog.html',context)
    return response
