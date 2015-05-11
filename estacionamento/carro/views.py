from django.shortcuts import render
from django.template import RequestContext, loader
from .forms import formCarro




def index(request):
    context = {'texto': 'index'}
        
    return render(request, 'index.html', context)

def formCadastroCarro(request):
    if request.method == 'POST':
        form = formCarro(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'carro.html', {'form': form})
    else:
        form = formCarro()

    return render(request, 'carro.html', {'form': form})


