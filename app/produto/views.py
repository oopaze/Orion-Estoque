from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Produto
from .forms import ProdutoForm


class ProdutosListView(ListView):
    title = "Produtos"
    template_name = "produto/list.html"
    model = Produto
    context_object_name = 'objects_data'
    ordering = "-criado_em"
    paginate_by = 10
    menu_section = "produtos"

    def get_columns(self):
        return (
            "ID", "Serial", "Marca", "Valor Compra", "Valor Revenda", "Modelo", "Descrição", "Ações"
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['columns'] = self.get_columns()
        ctx['title'] = self.title
        ctx['menu'] = self.menu_section
        ctx['model'] = self.model
        return ctx 


def detail_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    
    context = {
        "object": produto,
        "menu": "produtos",
        "title": "Detalhes do produto" 
    }
    return render(request, "produto/detail.html",context)
    

def create_produto(request):
    form = ProdutoForm(request.POST or None)
    
    context = {
        "form":form,
        "menu": "produtos",
        "title": "Novo produto",
        "model": Produto
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("list_produtos"))

        else:
            context['errors'] = form.errors
            
    return render(request, "default/form.html", context)


def update_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    context = {
        "object": produto, 
        "form": form,
        "menu": "produtos",
        "title": "Editar produto" 
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("list_produtos"))

        else:
            context['errors'] = form.errors

    return render(request, 'default/form.html', context)


def delete_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()

    return redirect(reverse("list_produtos"))