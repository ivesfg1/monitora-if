from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q

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


def get_site_queryset(query=None):
    queryset = []
    queries = query.split(" ")

    for q in queries:
        posts = User.objects.filter(Q(subject__name__icontains=q)).exclude(subject=None).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))


@login_required(login_url='/login/')
def monitores_list(request):

    query = ""
    if request.GET:
        query = request.GET['q']
        context = {
            'query': str(query)
        }

    context = {
        # 'monitores': User.objects.exclude(username=request.user.username).exclude(subject=None).all()
        'monitores': get_site_queryset(query)
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
            if request.user.check_password(form.cleaned_data['password']):
                # user = form.save()
                # user.set_password(form.cleaned_data['password'])
                # user.save()

                form.save()

                return redirect(reverse_lazy('home'))

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
def requests_create(request, pk):

    moni = get_object_or_404(User, id=pk)

    if moni == request.user:
        return redirect(reverse_lazy('home'))

    form = RequestForm(request.POST)

    if form.is_valid():

        requ = form.save()
        requ.requisitioner = request.user
        requ.teacher = moni
        requ.save()

        form = RequestForm()
        return redirect(reverse_lazy('home'))

    context = {
        'form': form,
        'monitor': moni
    }
    return render(request, 'core/requests-create.html', context)


@login_required(login_url='/login/')
def requests_detail(request, pk):

    req = get_object_or_404(Request, id=pk)

    context = {
        'request': req
    }
    return render(request, 'core/requests-detail.html', context)


@login_required(login_url='/login/')
def requests_update(request, pk):

    req = get_object_or_404(Request, id=pk)

    if req.requisitioner != request.user:
        return redirect(reverse_lazy('home'))

    form = RequestForm(instance=req)

    if request.method == 'POST':

        form = RequestForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))

    context = {
        'request': req,
        'form': form
    }
    return render(request, 'core/requests-update.html', context)


@login_required(login_url='/login/')
def requests_delete(request, pk):

    req = get_object_or_404(Request, id=pk)

    if req.teacher != request.user and req.requisitioner != request.user:
        return redirect(reverse_lazy('aulas'))

    if request.method == 'POST':
        req.delete()
        return redirect(reverse_lazy('aulas'))

    context = {
        'request': req
    }
    return render(request, 'core/requests-delete.html', context)


@login_required(login_url='/login/')
def aulas(request):

    context = {
        'requests_aluno': Request.objects.filter(requisitioner=request.user).all(),
        'requests_monitor': Request.objects.filter(teacher=request.user).all()
    }
    return render(request, 'aulas.html', context)


@login_required(login_url='/login/')
def home(request):

    context = {

    }
    return render(request, 'home.html', context)


@login_required(login_url='/login/')
def cadastro_monitor(request):

    form = CadastroMonitorForm(instance=request.user)
    if request.method == 'POST':

        form = CadastroMonitorForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():

            form.save()
            return redirect(reverse_lazy('home'))

    context = {
        'form': form
    }
    return render(request, 'cadastro-monitor.html', context)
