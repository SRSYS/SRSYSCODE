# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
from Mysqldb.models import Score_Graph

# 接收 Login 请求
def Login(request):
    Datebase_Return = ""
    ctx ={}
    if request.POST:
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
            
    return render(request, "index.html", ctx)
    
