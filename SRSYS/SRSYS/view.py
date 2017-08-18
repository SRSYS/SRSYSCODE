# -*- coding: utf-8 -*-
from django.shortcuts import render
from DjangoVerifyCode import Code
from Mysqldb.models import IMG

def code(request):
    code = Code(request)
    #code.img_width = 83
    #code.img_height = 30
    #code.font_color = ['black','darkblue','darkred']
    font_size = 30
    return code.display()
    
def index(request):    
    ctx ={}
    #广告读取
    Datebase_Advert_Return_1=IMG.objects.filter(Advert_Num=1)     #广告1
    for Advert_Var_1 in Datebase_Advert_Return_1:pass
    Datebase_Advert_Return_2=IMG.objects.filter(Advert_Num=2)     #广告2
    for Advert_Var_2 in Datebase_Advert_Return_2:pass
    ctx['Adverturl1'] = Advert_Var_1.Advert_url
    ctx['Adverturl2'] = Advert_Var_2.Advert_url
    ctx['Advertimg1'] = "/upload/"+str(Advert_Var_1.img)
    ctx['Advertimg2'] = "/upload/"+str(Advert_Var_2.img)
    return render(request, 'index.html',ctx)
