from importlib.metadata import requires

from django.contrib.auth import get_user_model
from django.forms import forms

user = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class":"form-control"}
        )
    )