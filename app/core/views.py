from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from produto.models import Produto


class HomeView(ListView, LoginRequiredMixin):
    title = "Produtos"
    template_name = "default/index.html"
    model = Produto
    context_object_name = 'objects_data'
    ordering = "-criado_em"
    paginate_by = 10
    menu_section = "home"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['menu'] = self.menu_section
        ctx['model'] = self.model
        return ctx 


home = HomeView.as_view()