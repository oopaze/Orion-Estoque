import json

from django.http.response import JsonResponse
from produto.models import Produto
from django.http import request
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.views.generic import ListView

from .models import Venda, VendaProduto
from .forms import VendaForm
from core.utils import get_bairros_choice, get_detail_instance
# Create your views here.

class VendasListView(ListView):
    title = "Vendas"
    template_name = "venda/list.html"
    model = Venda
    context_object_name = 'objects_data'
    ordering = "-criado_em"
    paginate_by = 10
    menu_section = "vendas"

    def get_columns(self):
        return (
            "ID", "Preço", "Quantidade", "Comprador", "Ações"
        )
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['columns'] = self.get_columns()
        ctx['title'] = self.title
        ctx['menu'] = self.menu_section
        ctx['model'] = self.model
        return ctx 


def detail_venda(request, id):
    venda = get_object_or_404(Venda, pk=id)

    context = {
        "object":venda,
        "menu":"vendas",
        "title":"Vendas",
        "attrs": get_detail_instance(venda, ['id'])
    }
    return render(request,"venda/detail.html",context)


def create_venda(request):
    form = VendaForm(request.POST or None )

    context = {
        "form":form,
        "menu":"vendas",
        "title": "Adicionar Venda"
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("list_vendas"))

        else:
            context['errors'] = form.errors

    return render(request, "venda/form.html",context)


def update_venda(request, id):
    venda = get_object_or_404(Venda, pk=id)
    form = VendaForm(request.POST or None, instance=venda)

    context = {
        "object": venda,
        "form":form,
        "menu":"vendas",
        "title":"Editar Venda",
        "model": Venda
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("list_vendas"))
        
        else:
            context['errors'] = form.errors

    return render(request, 'venda/form.html', context)


def get_bairros(request):
    cidade = request.GET.get('cidade', None)
    cidade = cidade.replace("_", " ").title().replace("D", "d")
    context = {
        "options": get_bairros_choice(cidade)
    }
    return render(request, "default/widgets/options.html", context)


def delete_venda(request, id):
    venda = get_object_or_404(Venda, pk=id)
    venda.delete()

    return redirect(reverse("list_vendas"))


def add_produto(request, id):
    venda = get_object_or_404(Venda, pk=id)

    context = {
        "object": venda,
        "produtos": Produto.objects.all(),
        "menu": "vendas",
        "has_add_button": True,
        "title": "Adicionar Produtos"
    }

    return render(request, 'venda/add_produtos.html', context)


def finalizar_venda(request, id):
    venda = get_object_or_404(Venda, pk=id)
    venda.save(save_close=True)

    return redirect(reverse("detail_venda", args=[venda.pk]))


@csrf_exempt
def add_produto_save(request, id):
    venda = get_object_or_404(Venda, pk=id)
    produtos = json.loads(list(request.POST.keys())[0])['produtos']

    produto_ids = [int(produto.get('id', -1)) for produto in produtos]

    instances = Produto.objects.filter(id__in = produto_ids)

    if request.method == 'POST':

        for instance in instances:
            quantidade = list(filter(
                lambda item: int(item['id']) == instance.id, produtos
            ))[0]['quantidade']

            venda_produto_instance = venda.vendaproduto_set.filter(produto_fk__id=instance.id)

            if venda_produto_instance.exists():
                venda_produto_instance = venda_produto_instance.first()
                venda_produto_instance.quantidade = quantidade
                venda_produto_instance.save()
                continue
            
            VendaProduto.objects.create(
                venda_fk=venda,
                produto_fk=instance,
                quantidade=quantidade,
            )

    return JsonResponse({"success": True})

