# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
from Mysqldb.models import Score_Graph

from DjangoVerifyCode import Code

# 接收 Login 请求
def Login(request):
    Datebase_Return = ""
    ctx ={}
    if request.POST:
        _code = request.POST['InputVerifyCode']
        
        if _code!=u'请输入验证码' or request.POST['InputStuNum']!=u'请输入十位考生号' or request.POST['InputName']!=u'请输入考生姓名':
            code = Code(request)
            if code.check(_code):
                try:
                    Datebase_Return=Score_Graph.objects.filter(StuNum=unicode(request.POST['InputStuNum']),NAME=unicode(request.POST['InputName']))
                    for var in Datebase_Return:pass
                    ctx['studentnum'] = var.StuNum
                    ctx['name'] = var.NAME
                    ctx['color'] = var.COLOR
                    ctx['sketch'] = var.SKETCH
                    ctx['linedraw'] = var.LINEDRAW
                    ctx['total'] = var.TOTAL
                    return render(request, "result.html", ctx)
                except:
                    ctx['ErrorMessage'] = u'账号或密码输入错误，请检查'
            else:
                ctx['ErrorMessage'] = u'验证码输入错误，请重新输入'
                
        else:ctx['ErrorMessage'] = u'未输入完整'
        
    return render(request, "index.html", ctx)
    
