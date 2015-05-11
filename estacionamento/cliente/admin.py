#coding:utf-8
from django.contrib import admin
from models import Cliente


class ClienteAdmin(admin.ModelAdmin):
	 list_display = ['nome','Carro','telefone','endereco']
	 list_filter = ['nome','telefone']
	 search_fields = ['nome']

	
admin.site.register(Cliente,ClienteAdmin) 
