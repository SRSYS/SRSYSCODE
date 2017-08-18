# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
 
class Score_Graph(models.Model):

    class Meta:
        verbose_name = "考生信息"
        verbose_name_plural = "分数数据库"

    StuNum = models.CharField(max_length=10,verbose_name="考生号")
    NAME = models.CharField(max_length=5,verbose_name="名称")
    COLOR = models.IntegerField(verbose_name="色彩")
    SKETCH = models.IntegerField(verbose_name="速写")
    LINEDRAW = models.IntegerField(verbose_name="素描")
    TOTAL = models.IntegerField(verbose_name="总分")


class IMG(models.Model):
    class Meta:
        verbose_name = "广告"
        verbose_name_plural = "广告"
    img = models.ImageField("广告图片(尺寸:325px*45px)",upload_to="advert")
    Advert_url = models.TextField(verbose_name="广告链接")
    Advert_Num = models.IntegerField(verbose_name="广告序号")
