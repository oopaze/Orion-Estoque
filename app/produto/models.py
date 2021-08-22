from django.db import models
from django.utils.timezone import now
from django.urls import reverse 


class Produto(models.Model):
    serial = models.CharField(max_length=30)
    tipo = models.CharField("Tipo de Produto", max_length=30, default="ssd")
    descricao = models.TextField(max_length=500)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    
    valor_compra = models.DecimalField(decimal_places=2,max_digits=10)
    valor_revenda = models.DecimalField(decimal_places=2,max_digits=10)
    quantidade = models.PositiveIntegerField()
    
    criado_em = models.DateField(auto_now_add=now)

    def __str__(self):
        return f"{self.tipo} ({self.modelo}) - {self.marca}"

    @staticmethod
    def get_list_url():
        return reverse("list_produtos") 

    @staticmethod
    def get_add_url():
        return reverse("create_produto") 

    def get_absolute_url(self):
        return reverse("update_produto", args=[self.id])

    def get_detail_url(self):
        return reverse("detail_produto", args=[self.id])

    def get_delete_url(self):
        return reverse("delete_produto", args=[self.id])