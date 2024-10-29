from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.decorators.csrf import csrf_protect
import re

# Create your views here.

# @login_required(login_url="/index")
def home(request):
    todas_mov = Movimentacoes.objects.all().order_by('-data_criacao')
    todas_contas = Conta.objects.all()
    return render(request,'home.html', {"movimentacoes": todas_mov, "contas": todas_contas})


def home_content(request):
    todas_mov = Movimentacoes.objects.all().order_by('-data_criacao')
    todas_contas = Conta.objects.all()
    return render(request,'home_content.html', {"movimentacoes": todas_mov, "contas": todas_contas})



def movimentacoes(request):
    todas_mov = Movimentacoes.objects.all().order_by('-data_criacao')
    todas_contas = Conta.objects.all()
    return render(request,'mov.html', {"movimentacoes": todas_mov, "contas": todas_contas})



def movimentacoes_content(request):
    todas_mov = Movimentacoes.objects.all().order_by('-data_criacao')
    todas_contas = Conta.objects.all()
    return render(request,'mov_content.html', {"movimentacoes": todas_mov, "contas": todas_contas})



def salvar_mov(request):
    if(request.method == "POST"):
        data = request.POST.get("data")    
        motivo = request.POST.get("motivo")
        
        valor = request.POST.get("valor")
        valor = re.sub(r'[^\d,]', '', valor)
        valor = valor.replace(',', '.')
        valor = float(valor)
        
        conta_id = request.POST.get("conta")
        conta = Conta.objects.get(external_id=conta_id)
        
        anexo = request.FILES.get('anexo')
        status = request.POST.get("status")
        
        consulta = Movimentacoes(data = data, motivo = motivo, valor = valor, conta = conta, anexo = anexo, status = status)
        consulta.save()
        dados = {
                'msg':"adicionado"
            }
        return JsonResponse(dados)
    
    else:
        return JsonResponse({"msg":"método inválido"})





# página das contas
def contas(request):
    
    if(request.method == "POST"):
        nome = request.POST.get('nome')
        nome = nome.strip()
        cidade_id = request.POST.get('cidade')
        cidade = Cidade.objects.get(external_id=cidade_id)
        ativo = request.POST.get('status')
        
        if(Conta.objects.filter(nome__iexact=nome).exists()):
            data = {
                "msg": "existente"
            }
            return JsonResponse(data)
        else:
            consulta = Conta(nome = nome, ativo=ativo, cidade = cidade)
            consulta.save()
            data = {
                'msg':"adicionado"
            }
            return JsonResponse(data)
    else:
        contas = Conta.objects.all()
        todas_cidades = Cidade.objects.all()
        return render(request,'contas.html', {"contas": contas,"cidades": todas_cidades})

def contas_content(request):
    todas_cidades = Cidade.objects.all()
    contas = Conta.objects.all()
    return render(request,'contas_content.html', {"contas": contas,"cidades": todas_cidades})






# página de ciadades
def cidades(request):
    if(request.method == 'POST'):
        nome = request.POST.get('nome')
        nome = nome.strip()
        ativo = request.POST.get('status')
        if(Cidade.objects.filter(nome__iexact=nome).exists()):
            data = {
                'msg': "existente"
            }
            return JsonResponse(data)
        
        else:
            consulta = Cidade(nome=nome, ativo=ativo)
            consulta.save()
            data = {
                'msg':"adicionado"
            }
            return JsonResponse(data)

    else:
        cidades = Cidade.objects.all()
        return render(request,'cidade.html',{"cidades":cidades})

def cidades_content(request):
    cidades = Cidade.objects.all()
    return render(request,'cidade_content.html', {"cidades": cidades})