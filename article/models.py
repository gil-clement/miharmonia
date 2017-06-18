#-*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

class Article(models.Model):
	title = models.CharField(max_length=200)
	desc = models.TextField()
	photo = models.ImageField(upload_to="photos/")
	prix = models.IntegerField()
	stock = models.IntegerField()
	delay = models.CharField(max_length=200)
	visible = models.BooleanField()	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
