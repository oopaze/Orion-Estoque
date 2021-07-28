from django.db import models
from django.utils.timezone import now


class Produto(models.Model):
    serial = models.CharField(max_length=30)
    armazenamento = models.CharField(max_length=10)
    descricao = models.TextField(max_length=500)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    
    valor_compra = models.DecimalField(decimal_places=2,max_digits=10)
    valor_revenda = models.DecimalField(decimal_places=2,max_digits=10)
    quantidade = models.PositiveIntegerField()
    
    criado_em = models.DateField(auto_now_add=now)

    def __str__(self):
        return f"{self.marca} - {self.armazenamento} - {self.modelo} - (R$ {self.valor_revenda})"