from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField("Email", unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def get_full_name(self):
        full_name = super().get_full_name()
        return full_name if full_name else self.email.split("@")[0]

    def get_first_letter(self):
        return self.get_full_name()[0].upper()