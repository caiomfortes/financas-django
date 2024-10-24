from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    return render(request,'cidade.html', {})

def cidades_content(request):
    return render(request,'cidade_content.html', {})