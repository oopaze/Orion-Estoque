from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from produto.models import Produto


class Venda(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    quantidade = models.PositiveIntegerField()
    desconto = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    endereco = models.CharField(max_length=150)
    comprador = models.CharField(max_length=50)
    criado_em = models.DateField(auto_now_add=now)

    def __str__(self):
        return f"{self.produto } - {self.quantidade} - {self.valor}"

    @staticmethod
    def get_list_url():
        return reverse("list_vendas")

    @staticmethod
    def get_add_url():
        return reverse("create_venda")
