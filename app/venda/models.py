from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from produto.models import Produto
from venda.choices import CIDADES, METODOS_PAGAMENTO


class Venda(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    desconto = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )
    produtos_fk = models.ManyToManyField(
        Produto, 
        verbose_name="Produtos", 
        through='VendaProduto', 
        through_fields=('venda', 'produto', 'quantidade', 'desconto'),
    )
    comprador = models.CharField("Nome do Cliente", max_length=50)
    tipo_de_contato = models.CharField("Tipo de Contato", max_length=200)
    contato = models.CharField("Telefone", max_length=50)
    email = models.CharField("Email", max_length=40, null=True, blank=True)

    pagamento = models.CharField("Método de Pagamento", max_length=50, choices=METODOS_PAGAMENTO)
    criado_em = models.DateField(auto_now_add=True)

    cidade = models.CharField("Cidade", max_length=50, choices=CIDADES)
    bairro = models.CharField("Bairro", max_length=50)
    cep = models.CharField("CEP", max_length=30)
    rua = models.CharField("Rua", max_length=100)
    numero = models.PositiveIntegerField("Nº")

    def __str__(self):
        return f"{self.pk} - {self.comprador} ({self.valor} R$)"

    @property
    def price(self):
        return f"{self.valor} R$"

    @staticmethod
    def get_list_url():
        return reverse("list_vendas")

    @staticmethod
    def get_add_url():
        return reverse("create_venda")

    def get_absolute_url(self):
        return reverse("update_venda", args=[self.id])

    def get_detail_url(self):
        return reverse("detail_venda", args=[self.id])

    def get_delete_url(self):
        return reverse("delete_venda", args=[self.id])


class VendaProduto(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.PROTECT, verbose_name="Produto"
    )
    venda = models.ForeignKey("Venda", on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField("Quantidade")
    desconto = models.PositiveIntegerField("Desconto")