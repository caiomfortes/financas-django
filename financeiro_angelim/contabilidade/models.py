from django.db import models
from django_hashids import HashidsField
import uuid
# Create your models here.


class Cidade(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    nome = models.CharField(max_length=50, verbose_name="Nome da cidade", unique=True)
    ativo = models.BooleanField(verbose_name="Ativo")
    
    class Meta:
        verbose_name = "cidade"
        verbose_name_plural = "cidades"
        
    def __str__(self):
        return self.nome
    

class Conta(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    nome = models.CharField(max_length=50, verbose_name="Nome da conta", unique=True)
    
    class Meta:
        verbose_name = "conta"
        verbose_name_plural = "contas"
    
    def __str__(self):
        return self.nome