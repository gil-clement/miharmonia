#-*- coding: utf-8 -*-#

from django.shortcuts import render
from article.forms import ArticleForm

def new_article (request):
	save= False
	if request.method == "POST":
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			article = Article()
			article.title = form.cleaned_data["title"]
			article.desc = form.cleaned_data["desc"]
			article.photo = form.cleaned_data["photo"]
			article.prix = form.cleaned_data["prix"]
			article.stock = form.cleaned_data["stock"]
			article.delay = form.cleaned_data["delay"]
			article.visible = form.cleaned_data["visible"]
			article.save()
	else:
		save = True
		form = ArticleForm()
	return render(request, 'article/newarticle.html',locals())
