# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from Mysqldb.models import Score_Graph

# Register your models here.



class Score_Graph_Show(admin.ModelAdmin):
    search_fields = ('StuNum', 'NAME')
    list_display_links =('StuNum', 'NAME')
    list_display = ('StuNum','NAME', 'COLOR','SKETCH','LINEDRAW','TOTAL')
     

admin.site.register(Score_Graph,Score_Graph_Show)


