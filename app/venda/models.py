from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now

from produto.models import Produto
from venda.services.telegram_bot import BotTelegram
from venda.choices import CIDADES, METODOS_PAGAMENTO, TIPO_CONTATO, VENDA_STATUS


class Venda(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    desconto = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True 
    )
    status = models.CharField("Status", max_length=50, choices=VENDA_STATUS, default="em_andamento")
    comprador = models.CharField("Nome do Cliente", max_length=50)
    responsavel = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True, blank=True)
    tipo_de_contato = models.CharField("Tipo de Contato", choices=TIPO_CONTATO, max_length=200)
    contato = models.CharField("Telefone", max_length=50)
    email = models.CharField("Email", max_length=40, null=True, blank=True)

    pagamento = models.CharField("Método de Pagamento", max_length=50, choices=METODOS_PAGAMENTO)
    criado_em = models.DateField(auto_now_add=True)

    cidade = models.CharField("Cidade", max_length=50)
    bairro = models.CharField("Bairro", max_length=50)
    cep = models.CharField("CEP", max_length=30)
    rua = models.CharField("Rua", max_length=100)
    numero = models.PositiveIntegerField("Nº")

    def __str__(self):
        return f"{self.pk} - {self.comprador} ({self.valor} R$)"

    def save(self, *args, **kwargs):
        save_close = kwargs.pop("save_close", None)

        if save_close:
            self.save_close()

        instance = super().save(*args, **kwargs)
        
        if save_close:
            self.send_telegram_message()

        return instance

    def save_close(self):
        for instance in self.vendaproduto_set.all():
            instance.calculate_produto_quantidade()
            instance.save()

        self.status = "a_caminho"

    def send_telegram_message(self):
        url_venda = f"{ settings.SITE_URL }{reverse('detail_venda', args=[self.pk])}"
        cidade = self.cidade.replace("_", " ").title()

        message = "Uma nova venda foi adicionada.\n\n" \
                  "Dados da Venda: \n" \
                 f"  Cliente: {self.comprador} \n  Telefone: {self.contato}\n" \
                 f"  Endereço: {self.rua} \n  Nº: {self.numero}\n" \
                 f"  Cidade: {cidade} \n  Bairro: {self.bairro}\n\n\n" \

        message += "Produtos: \n"
        for item in self.vendaproduto_set.all():
            message += f"    ({item.quantidade}) - {item.produto_fk}\n"
            
        message += f"\nTotalizando um valor de: {self.valor:.2f} R$ no {self.get_pagamento_display()}\n\n" \
                   "Por favor, entre no link abaixo para mais informações\n\n" \
                  f"URL: {url_venda}\n\n" \
                   "Orion Bot, \n" \
                   "Abraços!" \

        Bot = BotTelegram()
        Bot.send_message(
            message
        )

    def calculate_valor(self):
        valor = 0;
        for item in self.vendaproduto_set.all():
            valor += item.produto_fk.valor_revenda * item.quantidade;

        self.valor = valor
        self.save()

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
    produto_fk = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name="Produto"
    )
    venda_fk = models.ForeignKey("Venda", on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.PositiveIntegerField("Quantidade")
    desconto = models.PositiveIntegerField("Desconto", default=0)

    @property
    def valor(self):
        return self.produto_fk.valor_revenda * self.quantidade

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        self.venda_fk.calculate_valor()
        return instance

    def calculate_produto_quantidade(self):
        self.produto_fk.quantidade = self.produto_fk.quantidade - self.quantidade
        self.produto_fk.save()