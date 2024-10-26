from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

# @login_required(login_url="/index")
def home(request):
    return render(request,'home.html', {})

def home_content(request):
    return render(request,'home_content.html', {})

def movimentacoes(request):
    return render(request,'mov.html', {})

def movimentacoes_content(request):
    return render(request,'mov_content.html', {})

def contas(request):
    return render(request,'contas.html', {})

def contas_content(request):
    return render(request,'contas_content.html', {})



def cidades(request):
    if(request.method == 'POST'):
        nome = request.POST.get('nome')
        ativo = request.POST.get('status')
        if(Cidade.objects.filter(nome__iexact=nome).exists()):
            data = {
                'msg': "Esse nome já está em uso."
            }
            return JsonResponse(data)
        
        else:
            consulta = Cidade(nome=nome, ativo=ativo)
            data = {
                'msg':"Adicionado!"
            }
            return JsonResponse(data)

    else:
        return render(request,'cidade.html', {'msg':'teste'})

def cidades_content(request):
    return render(request,'cidade_content.html', {})