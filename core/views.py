from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView

from .models import *
from .forms import *


def index(request):

    # if request.user.is_authenticated:
    #     return redirect('monitores-detail', pk=request.user.pk)

    if request.user.is_authenticated:
        return redirect(reverse_lazy('home'))

    return render(request, 'index.html')


@login_required(login_url='/login/')
def monitores_list(request):

    context = {
        'monitores': User.objects.all()
    }
    return render(request, 'core/monitores.html', context)


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


@login_required(login_url='/login/')
def monitores_detail(request, pk):

    moni = get_object_or_404(User, id=pk)

    context = {
        'monitor': moni
    }
    return render(request, 'core/monitores-detail.html', context)


@login_required(login_url='/login/')
def monitores_update(request, pk):

    moni = get_object_or_404(User, id=pk)

    if moni != request.user:
        return redirect(reverse_lazy('index'))

    form = CadastroForm(instance=moni)

    if request.method == 'POST':

        form = CadastroForm(request.POST, request.FILES, instance=moni)
        if form.is_valid():

            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect(reverse_lazy('monitores'))

    context = {
        'monitor': moni,
        'form': form
    }
    return render(request, 'core/monitores-update.html', context)


@login_required(login_url='/login/')
def monitores_delete(request, pk):

    moni = get_object_or_404(User, id=pk)

    if moni != request.user:
        return redirect(reverse_lazy('index'))

    if request.method == 'POST':
        moni.delete()
        return redirect(reverse_lazy('index'))

    return render(request, 'core/monitores-delete.html')


@login_required(login_url='/login/')
def home(request):

    context = {
        'requests': Request.objects.filter(requisitioner=request.user).all()
    }

    return render(request, 'home.html', context)
