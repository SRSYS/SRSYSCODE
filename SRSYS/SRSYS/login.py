# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
from Mysqldb.models import Score_Graph
from Mysqldb.models import IMG
from DjangoVerifyCode import Code

# 接收 Login 请求
def Login(request):
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
    if request.POST:
        
        _code = request.POST['InputVerifyCode']
        
        if _code!='请输入验证码' or request.POST['InputStuNum']!='请输入十位考生号' or request.POST['InputName']!='请输入考生姓名':
            code = Code(request)
            if code.check(_code):
                try:
                    Datebase_Return=Score_Graph.objects.filter(StuNum=request.POST['InputStuNum'],NAME=request.POST['InputName'])
                    for var in Datebase_Return:pass
                    ctx['studentnum'] = var.StuNum
                    ctx['name'] = var.NAME
                    ctx['color'] = var.COLOR
                    ctx['sketch'] = var.SKETCH
                    ctx['linedraw'] = var.LINEDRAW
                    ctx['total'] = var.TOTAL
                    return render(request, "result.html", ctx)
                except:
                    ctx['ErrorMessage'] = '账号或密码输入错误，请检查'
            else:
                ctx['ErrorMessage'] = '验证码输入错误，请重新输入'
                
        else:ctx['ErrorMessage'] = '未输入完整'
        
    return render(request, "index.html", ctx)
    
