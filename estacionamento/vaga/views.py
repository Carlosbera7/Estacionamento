from django.shortcuts import render
from django.template import RequestContext, loader
from .forms import formVaga, formAlugar

# Create your views here.

def formCadastroVaga(request):
    if request.method == 'POST':
        form = formVaga(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'vaga.html', {'form': form})
    else:
        form = formVaga()

    return render(request, 'vaga.html', {'form': form})

def formCadastroAlugar(request):
    if request.method == 'POST':
        form = formAlugar(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'alugar.html', {'form': form})
    else:
        form = formAlugar()

    return render(request, 'alugar.html', {'form': form})    
