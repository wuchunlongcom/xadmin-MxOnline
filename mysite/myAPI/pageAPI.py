# -*- coding: utf-8 -*-
# pageAPI.py  分页类
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
PAGE_NUM = 25 #每页显示数
def toInt(c):
    try:
        i = int(c)
    except Exception as _e:
        i = 1
    return i
# 使用该函数步骤：2018.03.21
# 一、拷入文件：static/home/css/btn.css     templates/home/djangopage.html
# 二、在视图文件中
# 1、引用： from myAPI.pageAPI import djangoPage,PAGE_NUM,toInt
# 2、方法：def show(request):  -->   def show(request, page):
# 3、在返回html前台以前加入下列两条语句，其中blogs数据库记录或列表。
#      blog_list, pageList, paginator, page = djangoPage(blogs,page,PAGE_NUM)  #调用分页函数
#      offset = PAGE_NUM * (page - 1)
# 4、在html前台文件中加入分布：<div style="padding-left:520px;"">{% include 'home/djangopage.html' %}  </div> <!--分页--> 
# 三、更改路由：r'^show/'      -->        r'^show/(?P<page>\d*)?$'
#适用django分页  1、contact_list数据库记录或列表；2、page当前页；3、设置每页显示数 num
# 综合应用实例：http://localhost:8000/accountTest/billing/
def djangoPage(contact_list,page,num):
    paginator = Paginator(contact_list, num) 
    page = toInt(page) 
    try:
        model_list = paginator.page(page)
    except PageNotAnInteger:
        model_list = paginator.page(1)
    except EmptyPage:
        model_list = paginator.page(paginator.num_pages)
         
    pageList = list(paginator.page_range)
    if page < (paginator.num_pages)-3:
        pageList[page+2:-1] = ['...']
    if page > 1+3:
        pageList[1:page-3] = ['...']        
    #print('paginator.num_pages=',paginator.num_pages)
    return model_list,pageList,paginator.num_pages,page
