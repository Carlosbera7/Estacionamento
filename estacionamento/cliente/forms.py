from django.forms import ModelForm
from models import Cliente

class formCliente(ModelForm):
	class Meta:
		model=Cliente
		fields=['nome','telefone','endereco','Carro']