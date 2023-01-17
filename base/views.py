from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render (request, 'inicio.html')

def contato(request):
    contexto = {
        'telefone': '(18)997974147',
        'responsavel': 'Eder Assis'
    }
    return render(request, 'contato.html', contexto)