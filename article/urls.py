#-*- coding: utf-8 -*-#

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^nuevo-article/$', views.new_article, name='new_article'),
]
