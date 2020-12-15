from django import forms

from .models import *


class CadastroForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:

        model = User
        fields = ('photo', 'registration', 'username', 'facebook', 'twitter', 'instagram', 'subject')


class RequestForm(forms.ModelForm):

    class Meta:

        model = Request
        # fields = ('teacher', 'comment')
        fields = ('comment',)


class CadastroMonitorForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ('subject',)
