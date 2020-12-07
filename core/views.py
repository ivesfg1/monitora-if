from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')


@login_required
def monitores_list(request):

    context = {
        'monitores': User.objects.all()
    }
    return render(request, 'core/monitores.html', context)

# lembrar de botar la no template de list dnv na parte do h4 <a href="{% url 'monitores-detail' user.pk %}">


def monitores_create(request):

    if request.user.is_authenticated:
        return redirect(reverse_lazy('index'))

    form = CadastroForm(request.POST, request.FILES)
    if form.is_valid():

        # user = User(**form.cleaned_data)

        # user.photo = form.cleaned_data["photo"]
        # user.registration = form.cleaned_data["registration"]
        # user.username = form.cleaned_data["username"]
        # user.set_password(form.cleaned_data["password"])

        # user.save()

        # ↴ maneira mais compacta de se fazer a mesma coisa.

        user = form.save()
        user.set_password(form.cleaned_data["password"])
        user.save()

        form = CadastroForm()
        return redirect(reverse_lazy('login'))

    context = {
        'form': CadastroForm()
    }

    return render(request, 'cadastro.html', context)
