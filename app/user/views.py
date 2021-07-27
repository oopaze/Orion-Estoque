from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = CustomAuthenticationForm

    def form_invalid(self, form):
        for key in form.errors.keys():
            messages.error(self.request, form.errors[key])

        return super().form_invalid(form)


