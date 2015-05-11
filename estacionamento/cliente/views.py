from django.shortcuts import render
from django.template import RequestContext, loader
from .forms import formCliente

def formCadastroCliente(request):
    if request.method == 'POST':
        form = formCliente(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cliente.html', {'form': form})
    else:
        form = formCliente()

    return render(request, 'cliente.html', {'form': form})

# Create your views here.
