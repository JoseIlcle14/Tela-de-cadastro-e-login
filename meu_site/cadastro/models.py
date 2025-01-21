from django.db import models
from django.core.validators import MinLengthValidator

class UsuariosCadastrados(models.Model):
    nome_completo = models.CharField(max_length= 300, null=True, blank=True)
    email = models.EmailField(max_length= 300, null=True, blank=True, unique=True)
    senha = models.CharField(
        max_length= 128,
        validators= [MinLengthValidator(8)]
    )
    
    def __str__(self):
        return self.nome_completo