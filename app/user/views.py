from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls.base import reverse

from .forms import CustomAuthenticationForm, UserChangeForm
from core.utils import get_detail_instance

class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = CustomAuthenticationForm

    def form_invalid(self, form):
        for key in form.errors.keys():
            messages.error(self.request, form.errors[key])

        return super().form_invalid(form)


@login_required
def user_detail_view(request):
    ignore_fields = [
        'password', 'id', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined'
    ]
    context = {
        "object": request.user,
        "menu": "user",
        "dont_delete": True,
        "title": "Detalhes do Usuário",
        "attrs": [
            {
                "label": "Nome",
                "value": request.user.get_full_name()
            },
            {
                "label": "Email",
                "value": request.user.email
            },
            {
                "label": "Nome do Usuário",
                "value": request.user.username
            }
        ]
    }
    return render(request, "user/detail.html",context)
    

def update_user(request):
    form = UserChangeForm(request.POST or None, instance=request.user)

    context = {
        "object": request.user, 
        "form": form,
        "menu": "user",
        "title": "Editar Usuário" 
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("self_detail_user"))

        else:
            context['errors'] = form.errors

    return render(request, 'default/form.html', context)