# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.http import JsonResponse  

# Create your views here.
from django.http import HttpResponse
from . import models


def posts_act(request):
	eid = request.GET.get('eid','')                 # 发布会id
	status = request.GET.get('status','')           # 状态

	print 'eid: ',eid
	print 'status: ',status

	if eid =='' or status == '' :
		return JsonResponse({'status':10021,'message':'parameter error'})

	data = {
		'eid':eid,
		'status':status,
		'msg':'This msg is from Server.'
	}

	return JsonResponse(data)

def posts_post(request):
	eid = request.POST.get('eid','')                 # 发布会id
	status = request.POST.get('status','')           # 状态

	print 'eid: ',eid
	print 'status: ',status

	if eid =='' or status == '' :
		return JsonResponse({'status':10021,'message':'parameter error'})

	data = {
		'eid':eid,
		'status':status,
		'msg':'This is Server.'
	}

	return JsonResponse(data)
    # return JsonResponse({'status':200,'message':'add event success'})


def posts_home(request):
	queryset = models.Post.objects.all()
	data = {
		# "queryset": queryset,
		"name": "home",
		"age": "18",
	}
	return JsonResponse(data)
	# return redirect(reverse("detail",kwargs={"id":3}))
	# return render(request,"base.html",data)
	# return redirect("detail",id=3)
	# return redirect("/post/3/")

# def posts_home(request):
# 	context = {
# 		"title": "home"
# 	}
# 	return render(request,"base.html",context)

def posts_detail(request,id=None):
	# obj = models.Post.objects.get(id=3)
	obj = get_object_or_404(models.Post,id=id)
	data = {
		"obj":obj
	}

	return render(request,"detail.html",data)

# def posts_detail(request):
# 	# obj = models.Post.objects.get(id=3)
# 	obj = get_object_or_404(models.Post,id=1)
# 	data = {
# 		"obj":obj
# 	}

# 	return render(request,"detail.html",data)

def posts_create(request):
	context = {
		"title": "create"
	}
	return render(request,"index.html",context)

# def posts_home(request):
# 	return render(request,"index.html")

# def posts_home(request):
# 	return HttpResponse("Hello World!")

# def posts_create(request):
# 	return HttpResponse("<h1>posts_create</h1>")

def posts_update(request):
	return HttpResponse("<h1>posts_update</h1>")

# def posts_detail(request):
# 	return HttpResponse("<h1>posts_detail</h1>")

def posts_delete(request):
	return HttpResponse("<h1>posts_delete</h1>")


from django.views.generic import ListView
class PostList(ListView):
	"""post的视图类"""

	def get(self,request):
		return HttpResponse("<h1>post的视图类</h1>") 