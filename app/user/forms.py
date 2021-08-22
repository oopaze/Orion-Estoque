from django.contrib.auth.forms import AuthenticationForm
from django import forms

from user.models import User


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs.update({
                "placeholder": "Email" if key == 'username' else "Senha"
            })


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")