from django.shortcuts import render
from django.template import RequestContext, loader
from .forms import formVaga, formAlugar
from models import Vaga

# Create your views here.

def formCadastroVaga(request, id=None):
	if id:
		obj = get_object_or_404(Carro, pk=id)
	else:
		obj = None	
	if request.method == 'POST':
		form = formVaga(request.POST,instance = obj)
		if form.is_valid():
			form.save()
			q = Vaga.objects.all()
			context = {
			'ListaVagas': q,
			}
			return render(request, 'viz_vagas.html', context)
	else:
		form = formVaga(instance = obj)
	return render(request, 'vaga.html', {'form': form})

def formCadastroAlugar(request):
    if request.method == 'POST':
        form = formAlugar(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form})
    else:
        form = formAlugar()

    return render(request, 'alugar.html', {'form': form})    


def ListaVagasCadastradas(request):
	if request.method == 'POST':
		query = request.POST.get('parametro')
		q = Vaga.objects.filter(numero__contains=query)
	else:
		q = Vaga.objects.all()
	context = {
	'ListaVagas': q,
	}
	return render (request,'viz_vagas.html',context)
