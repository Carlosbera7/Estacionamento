from django.shortcuts import render
from django.template import RequestContext, loader
from .forms import formCliente
from models import Cliente


def formCadastroCliente(request):
    if request.method == 'POST':
        form = formCliente(request.POST)
        if form.is_valid():
        	form.save()
        	q = Cliente.objects.all()
        	context = {
        	'ListaClientes': q,
        	}
        	return render(request, 'viz_cliente.html', context)
    else:
        form = formCliente()

    return render(request, 'cliente.html', {'form': form})

def ListaClientesCadastrados(request):
	if request.method == 'POST':
		query = request.POST.get('parametro')
		q = Cliente.objects.filter(nome__contains=query)
	else:
		q = Cliente.objects.all()
	context = {
	'ListaClientes': q,
	}
	return render (request,'viz_cliente.html',context)

# Create your views here.
