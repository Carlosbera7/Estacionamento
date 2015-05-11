from django.forms import ModelForm
from models import Vaga, Alugar

class formVaga(ModelForm):
	class Meta:
		model=Vaga
		fields=['numero','localizacao']

class formAlugar(ModelForm):
	class Meta:
		model=Alugar
		fields=['Carro','Cliente','vaga','valor','tempo']		