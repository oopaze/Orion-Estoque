from django import forms
from django.db.models import fields

from .models import Venda
from venda.choices import BAIRROS


class VendaForm(forms.ModelForm):
    bairro = forms.ChoiceField(
        label="Bairro", 
        choices=BAIRROS
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Venda
        fields = (
            "comprador",
            "tipo_de_contato",
            "contato",
            "email",
            'cidade',
            'bairro', 
            'cep', 
            'rua', 
            'numero'
        )