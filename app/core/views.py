from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from produto.models import Produto


@login_required
def home(request):
    context = {
        "title": "Home",
        "menu": "home",
    }
    return render(request, 'default/index.html', context)
