from django import forms

from .models import *


class CadastroForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:

        model = User
        fields = ('photo', 'registration', 'username')
