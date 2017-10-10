# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from posts import models

class PostAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ["title","content"]
	list_display_links = ["title"]
	list_filter = ["timestamp","content"]
	search_fields = ["title","content"]
	list_editable = ["content"]
	# def __init__(self, arg):
	# 	super(PostAdmin, self).__init__()
	# 	self.arg = arg

	class Meta:
		model = models.Post
		

admin.site.register(models.Post,PostAdmin)
