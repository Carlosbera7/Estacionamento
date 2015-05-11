from django.forms import ModelForm
from models import Carro

class formCarro(ModelForm):
	class Meta:
		model=Carro
		fields=['modelo','cor','marca','placa']