from django.shortcuts import render
from base.forms import ContatoForm

def inicio(request):
    return render (request, 'inicio.html')

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(18)997974147',
        'responsavel': 'Eder Assis',
        'form': form,
        'sucesso': sucesso
    }
    
    return render(request, 'contato.html', contexto)