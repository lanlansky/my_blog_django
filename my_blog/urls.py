"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home', home),
    #^(?P<my_args>\d+)/$这个正则表达式的意思是将
    #传入的一位或者多位数字作为参数传递到views中的detail作为参数, 其中?P<my_args>定义名称用于标识匹配的内容
    #http://127.0.0.1:8000/1000/
	#http://127.0.0.1:8000/9/ 都可以匹配
    #url(r'^(?P<my_args>\d+)/$', detail),
    #url(r'^test', test),
]
