from django.db import models
from django_hashids import HashidsField
import uuid
import datetime
import os
# Create your models here.



class Cidade(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    nome = models.CharField(max_length=50, verbose_name="Nome da cidade", unique=True, null=False, blank=False)
    ativo = models.BooleanField(verbose_name="Ativo", default=True, null=False, blank=False)
    
    class Meta:
        verbose_name = "cidade"
        verbose_name_plural = "cidades"
        
    def __str__(self):
        return self.nome
    

class Conta(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    nome = models.CharField(max_length=50, verbose_name="Nome da conta", unique=True, null=False, blank=False)
    ativo  = models.BooleanField(verbose_name="Ativo", default=True, null=False, blank=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, verbose_name="Cidade")
    
    class Meta:
        verbose_name = "conta"
        verbose_name_plural = "contas"
    
    def __str__(self):
        return self.nome
    
    

class Movimentacoes(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    data = models.DateField(verbose_name="Data de pagamento", null=False, blank=False)
    motivo = models.TextField(verbose_name="Motivo", null=False, blank=False)
    valor = models.DecimalField(verbose_name="Valor", max_digits=14, decimal_places=2, null=False, blank=False)
    conta = models.ForeignKey(Conta, verbose_name="Conta", on_delete=models.SET_NULL, null=True, blank=False)
    anexo=models.FileField(verbose_name="Anexo", upload_to="anexo_mov/%Y/%m", max_length=100, null=True, blank=True)
    status = models.CharField(verbose_name="Status", max_length=15, null=False, blank=False)
    data_criacao = models.DateField(verbose_name="Data de criação", auto_now_add=True, blank=False, null=False)

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"

    def __str__(self):
        return self.motivo
    
    def pasta_arquivo(self):
        """Retorna o caminho da pasta do arquivo"""
        caminho_completo = self.arquivo.path
        data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_completo))
        ano = data_modificacao.year
        mes = data_modificacao.month
        pasta_arquivo = f"media/{ano}/{mes:02d}"  # Formatação com zeros à esquerda para o mês
        return pasta_arquivo
    
