# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
 
class Score_Graph(models.Model):
    NAME = models.TextField()
    COLOR = models.IntegerField()
    SKETCH = models.IntegerField()
    LINEDRAW = models.IntegerField()
    TOTAL = models.IntegerField()
