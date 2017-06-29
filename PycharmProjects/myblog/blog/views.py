# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from . import models

def index(request):
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def add_article(request):
    return render(request,'blog/add_article.html')

def add_action(request,):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    # title = request.POST['title']
    # content = request.POST['content']
    models.Article.objects.create(title=title,content=content)
    return HttpResponseRedirect('/blog')

def edit_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})

def edit_action(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article.title = title
    article.content = content
    article.save()
    return HttpResponseRedirect('/blog/article/'+article_id)