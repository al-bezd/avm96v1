#unicode:utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#from django.forms import forms
from django import forms


rep1='Здравсвуйте! мы рады приветствовать вас на нашем сайте, задайте мне вопрос мы будем рады ответить вам!'
rep2='Как вы хотите что бы мы вам ответили? Если хотите что бы мы вам позвонили то просто напишите свой номер, а если хотите что бы ответ пришел вам на почту то просто напишите свой вопрос а адрес электронной почты оставьте в скобочках, вот так (myemail@domain.com), Спасибо за то что с нами ;) '
rep3='Благоарим ва за вопрос, наши специалисты ответят вам на вопрос через 15 минут '
class ChatConsultant(models.Model):
    class Meta():
        verbose_name_plural = 'Чат консультант'
        verbose_name = 'Чат консультант'
    name=models.CharField(max_length=60, verbose_name='ФИО Консультанта',unique=True)
    rang=models.CharField(verbose_name='Должность', default='дежурный менеджер', max_length=60)
    img=models.ImageField(verbose_name='Фото(54x54)', blank=True, null=True,height_field=54,width_field=54)
    rep1=models.TextField(verbose_name='Приветственная реплика', default=rep1)
    rep2=models.TextField(verbose_name='Hеплика ответа', default=rep2)
    rep3=models.TextField(verbose_name='Завершающая реплика', default=rep3)
    #new 05102017
    status = models.BooleanField(default=True, verbose_name='Включить ЧатБота')

    def prew_img(self):
        if self.img:
            return '<img src="%s" width="54">' % self.img.url
        else:
            return u'(Нет картинки)'

    prew_img.short_description = u'Изображение'
    prew_img.allow_tags = True
    def __unicode__(self):
        return ('%s(%s)')%(self.name,self.rang)

class UserTalker(models.Model):
    id_user=models.CharField(max_length=255, verbose_name=u'ID пользователя')
    status=models.CharField(max_length=255,verbose_name=u'Статус')

    def __unicode__(self):
        return ('%s(%s)')%(self.status,self.id_user)

class ChatRoom(models.Model):
    class Meta():
        verbose_name_plural = 'Чат'
        verbose_name = 'Чат'
    id_room=models.IntegerField(verbose_name=u'ID Чата',blank=True,null=True)
    date_create=models.DateTimeField(auto_now_add=True,verbose_name=u'Дата созданния')
    comment = models.TextField(blank=True, null=True, verbose_name=u'Коммент',)

    comment.formfield(widget=forms.Textarea(attrs={'rows': 20, 'cols': 80}))


    def save(self, *args, **kwargs):
        #ChatRoom.objects.filter(id_room=self.id_room).order_by('date_create').delete()
        super(ChatRoom, self).save()

    def update_chat_room(self, *args, **kwargs):
        try:
            if ChatRoom.objects.get(id_room=self.id_room):
                c=ChatRoom.objects.get(id_room=self.id_room)
                c.comment=self.comment
                c.id_room=self.id_room
                c.save()
            else:
                print "!!! lose !!!"
        except:
            super(ChatRoom, self).save()



    def __unicode__(self):
        return ('%s')%(self.id_room)

class MyForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields=(
            'id_room',
            #'date_create',
            'comment'
        )
    widgets = {'comment': forms.Textarea(attrs={'rows':20, 'cols':80}),}

'''class ChatSetting(models.Model):
    class Meta():
        verbose_name_plural = 'Настройки'
        verbose_name = 'Настройки'
    title=models.CharField(max_length=50,verbose_name='Настройки',default='Настройка чат бота')
    status=models.BooleanField(default=True,verbose_name='Включить ЧатБота')
    def __unicode__(self):
        return ('%s')%(self.title)'''
try:
    c=ChatConsultant(name=u'Светлана Владимировна')
    c.save()
except:
    pass