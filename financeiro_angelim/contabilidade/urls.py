from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("home", home, name="home"),
    path("home/content",home_content,name="home"),
    path("mov", movimentacoes, name="movimentacoes"),
    path("mov/content", movimentacoes_content, name="movimentacoes"),
    path("contas", contas, name="contas"),
    path("contas/content", contas_content, name="contas"),
    path("cidades", cidades, name="cidades"),
    path("cidades/content", cidades_content, name="cidade"),
]