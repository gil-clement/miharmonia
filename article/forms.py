#-*- coding: utf-8 -*

from django import forms

class ArticleForm(forms.Form):
	title= forms.CharField(max_length=200, widget=forms.TextInput({ "placeholder": "pone el titulo aqui" }))
	desc=forms.CharField(widget=forms.Textarea)
	photo=forms.ImageField()
	prix= forms.IntegerField(label='Pone el precio aqui')
	stock = forms.IntegerField(label='pone la quatidad en stock aqui')
	delay = forms.CharField(max_length=200, label='Pone el tiempo para enviar')
	visible = forms.BooleanField(help_text='check ese si quieres que el articulo esta visible ',required='false')
