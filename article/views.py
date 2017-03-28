from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
# Create your views here.
def home(request):
	post_list=Article.objects.all()
	#render()函数中第一个参数是request 对象, 第二个参数是一个模板名称，
	#第三个是一个字典类型的可选参数. 它将返回一个包含有给定模板根据给定的上下文渲染结果
	#的 HttpResponse对象。
	return render(request,'home.html',{'post_list':post_list})
	
