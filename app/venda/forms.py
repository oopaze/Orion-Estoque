from django import forms
from .models import Venda


class VendaForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        commit = kwargs.pop("commit",None)
        kwargs['commit'] = False

        instance = super().save(*args, **kwargs)
        instance.valor = (
            float(instance.produto.valor_revenda) * instance.quantidade
        ) * (1 - (instance.desconto / 100))

        if not commit:
            instance.save()

        return instance

                


    class Meta:
        model = Venda
        exclude = ["criado_em", "valor"]