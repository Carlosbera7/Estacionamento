#coding:utf-8
from django.db import models
from carro.models import Carro

# Create your models here.

class Cliente(models.Model):
	nome = models.CharField('Nome',max_length=100,null=True)
	telefone = models.CharField('Telefone',max_length=15,null=True)
	endereco = models.CharField('Endereço',max_length=100,null=True)
	Carro = models.ForeignKey(Carro,verbose_name="Carro",null=True)
	
	def __unicode__(self):
		return self.nome
	
