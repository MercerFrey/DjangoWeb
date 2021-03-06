# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def article_list(request):
    # order not so important
    articles = Article.objects.all().order_by('date')

    return render(request, "articles/article_list.html",{'articles': articles})

def article_detail(request, slug):
    #return HttpResponse(slug);
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',{'article': article})
