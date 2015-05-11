#coding:utf-8
from django.contrib import admin
from models import Carro


class CarroAdmin(admin.ModelAdmin):
	 list_display = ['modelo','cor','marca','placa']
	 list_filter = ['modelo','marca']
	 search_fields = ['marca']

	
admin.site.register(Carro,CarroAdmin) 
