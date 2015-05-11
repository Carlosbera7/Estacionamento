#coding:utf-8
from django.contrib import admin
from models import Vaga, Alugar


class VagaAdmin(admin.ModelAdmin):
	 list_display = ['numero','localizacao']
	 list_filter = ['numero','localizacao']
	 search_fields = ['numero']
	 
class AlugarAdmin(admin.ModelAdmin):
	list_display = ['valor','tempo']
	list_filter = ['valor','tempo']
	search_fields = ['valor']
	 


	
admin.site.register(Vaga,VagaAdmin)
admin.site.register(Alugar,AlugarAdmin) 
