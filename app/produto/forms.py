from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        commit = kwargs.pop("commit", None)
        kwargs['commit'] = False

        instance = super().save(*args, **kwargs)
        instance.valor_revenda = float(instance.valor_compra) * 1.5

        if not commit:
            instance.save()

        return instance


    class Meta:
        model = Produto
        exclude = ["criado_em", "valor_revenda"]