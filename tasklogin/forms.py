from django import forms
from tasklogin.models import Login
from django.forms import fields

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"