from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User


class Registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "address", "username",
                  "password1", "password2", "email", "company"]
