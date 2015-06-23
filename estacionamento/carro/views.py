from django.shortcuts import render
from django.template import RequestContext, loader
from .forms import formCarro
from models import Carro

def index(request):
	return render(request, 'index.html')

def formCadastroCarro(request):
	if request.method == 'POST':
		form = formCarro(request.POST)
		if form.is_valid():
			form.save()
			q = Carro.objects.all()
			context = {
			'listaCarros': q,
			}	

		return render(request, 'viz_carros.html', context)
	else:
		form = formCarro()
	return render(request, 'carro.html', {'form': form})
    
def ListaCarrosCadastrados(request):
	if request.method == 'POST':
		query = request.POST.get('parametro')
		q = Carro.objects.filter(modelo__contains=query)
	else:
		q = Carro.objects.all()
	context = {
	'listaCarros': q,
	}
	return render (request,'viz_carros.html',context)
