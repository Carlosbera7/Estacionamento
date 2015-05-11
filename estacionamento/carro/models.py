#coding:utf-8
from django.db import models

# Create your models here.

class Carro(models.Model):
	modelo = models.CharField('Modelo',max_length=50,null=True)
	cor = models.CharField('Cor',max_length=20,null=True)
	marca = models.CharField('Marca',max_length=50,null=True)
	placa = models.CharField('Placa',max_length=10,null=True)
	
	def __unicode__(self):
		return self.modelo
	

	
	
