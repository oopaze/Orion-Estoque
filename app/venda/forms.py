from django import forms
from django.db.models import fields

from .models import Venda
from venda.choices import BAIRROS


class VendaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsavel'].required = True
            

    class Meta:
        model = Venda
        fields = (
            "responsavel",
            "comprador",
            "tipo_de_contato",
            "contato",
            "email",
            "cidade",
            "bairro", 
            "cep", 
            "rua", 
            "numero",
        )


class MetodoPagamentoVendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ('pagamento',)