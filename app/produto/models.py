from django.db import models

# Create your models here.

class Produto(models.Model):
    serial = models.CharField(max_length=30)
    armazenamento = models.CharField(max_length=10)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    valor_compra = models.DecimalField(decimal_places=2,max_digits=10)
    valor_revenda = models.DecimalField(decimal_places=2,max_digits=10)
    quantidade = models.PositiveIntegerField()
    create_at = models.DateField()

    def __str__(self):
        return f"{self.marca} - {self.armazenamento} - {self.modelo} - (R$ {self.valor_revenda})"