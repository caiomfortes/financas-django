from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from contabilidade.views import home


def index(request):
    return render(request,'index.html', {})


def signup(request):
    return render(request,'signup.html', {})


def redirect_login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        # Se a autenticação falhar, redireciona ou exibe um erro
        return render(request, 'index.html', {'error': 'Credenciais inválidas.'})


def logout_view(request):
    logout(request)