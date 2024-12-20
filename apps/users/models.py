from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    OPCOES_DOCS = [
        ("CPF", "CPF"),
        ("CNPJ", "CNPJ"),
    ]
    
    # Extensão do modelo User
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    telefone = models.CharField(
        max_length=15,
        null=False,
        blank=False
    )
    
    data_nascimento = models.DateField(
        null=False,
        blank=False
    )
    
    tipo_doc = models.CharField(
        choices=OPCOES_DOCS,
        max_length=10,
        null=False,
        blank=False
    )
    
    documento = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    
    def __str__(self):
        return self.usuario.username
