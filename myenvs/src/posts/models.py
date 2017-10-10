# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 帖子
class Post(models.Model):
	title = models.CharField(max_length=256) # 标题，存文字的
	content = models.TextField() # 内容
	update = models.DateTimeField(auto_now=True,auto_now_add=False) # 更新时间
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True) #创建时间
	
	def __str__(self): # python3
		return self.title
	
	def __unicode__(self): #python2
		return self.title
