from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Produto
from .forms import ProdutoForm


def list_produtos(request):
    produtos = Produto.objects.all()
    
    context = {
        "objects":produtos,
        "menu": "produtos",
        "title": "Produtos" 
    }

    return render(request, "default/list.html", context)


def detail_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    
    context = {
        "object":produto,
        "menu": "produtos",
        "title": "Detalhes do produto" 
    }
    return render(request, "produto/detail.html",context)
    

def create_produto(request):
    form = ProdutoForm(request.POST or None)
    
    context = {
        "form":form,
        "menu": "produtos",
        "title": "Novo produto" 
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