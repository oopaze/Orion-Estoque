from django.http import request
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.urls import reverse
from django.views.generic import ListView

from .models import Venda
from .forms import VendaForm
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
        "menu":"produto",
        "title":"Produto"
    }
    return render(request,"venda/detail.html",context)

def create_venda(request):
    form = VendaForm(request.POST or None )

    context = {
        "form":form,
        "menu":"vendas",
        "title": "Nova Venda"
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("list_vendas"))

        else:
            context['errors'] = form.errors

    return render(request, "default/form.html",context)

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

    return render(request, 'default/form.html', context)

def delete_venda(request, id):
    venda = get_object_or_404(Venda, pk=id)
    venda.delete()

    return redirect(reverse("list_vendas"))

