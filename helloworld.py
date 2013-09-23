#!/usr/bin/python
#-*-coding:utf8-*-
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse('Hello, Django!')

def me(request):
	now = datetime.datetime.now()  
	html = "It is now %s." % now 
	return HttpResponse(html);