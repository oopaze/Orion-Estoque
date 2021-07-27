from django.db import models
from produto.models import Produto
# Create your models here.
class Venda(models.Model):
    create_at = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    quantidade = models.PositiveIntegerField()
    desconto = models.PositiveIntegerField(default=0)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    endereco = models.CharField(max_length=150)
    comprador = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.produto } - {self.quantidade} - {self.valor}"
