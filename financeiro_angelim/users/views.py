from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .models import *
from django.http import JsonResponse



def index(request):
    if(request.method == "POST"):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"msg": "sucesso"})
        else:
            # Se a autenticação falhar, redireciona ou exibe um erro
            return render(request,'index.html', {})
    else:
        return render(request,'index.html', {})


def signup(request):
    return render(request,'signup.html', {})

def logout_view(request):
    logout(request)
    return redirect("index")