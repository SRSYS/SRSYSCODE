# -*- coding: gb2312 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
import sqlite3

#�����ݿ��ļ�
conn = sqlite3.connect('.//Database//Score_Graph.db',check_same_thread = False)
conn.text_factory = bytes
print "Opened Database Successfully!!"
database = conn.cursor()    #���

# ���� Login ����
def Login(request):
    ctx ={}
    #return render(request, "index.html")
    if request.POST:
        try:
            cursor = database.execute("SELECT COLOR,SKETCH,LINEDRAW,TOTAL  from Score_Graph where Name='"+str(request.POST['InputName'])+"' and StuNum="+str(request.POST['InputStuNum']))
            for row in cursor:pass
            ctx['name'] = request.POST['InputName']
            ctx['studentnum'] = request.POST['InputStuNum']
            ctx['color'] = row[0]
            ctx['sketch'] = row[1]
            ctx['linedraw'] = row[2]
            ctx['total'] = row[3]
            return render(request, "result.html", ctx)
        except:
            ctx['ErrorMessage'] = u'�˺Ż����������������'
    return render(request, "index.html", ctx)
    
