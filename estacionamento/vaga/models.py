#coding:utf-8
from django.db import models
from cliente.models import Cliente
from carro.models import Carro


# Create your models here.

class Vaga(models.Model):
	numero = models.CharField('Numero',max_length=10,null=True)
	localizacao = models.CharField('Localização',max_length=100,null=True)	
	
	def __unicode__(self):
		return self.numero
		
class Alugar(models.Model):
	Carro = models.ForeignKey(Carro,verbose_name="Carro",null=True)
	Cliente = models.ForeignKey(Cliente,verbose_name="Cliente",null=True)
	vaga = models.ForeignKey(Vaga,verbose_name="Vaga",null=True)	
	valor = models.CharField('Valor',max_length=15,null=True)
	tempo = models.CharField('Tempo',max_length=10,null=True)
	
