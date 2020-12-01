from django.shortcuts import render

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *


class IndexView(TemplateView):

    template_name = "index.html"


class AulasView(TemplateView):

    template_name = "aulas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class MonitoresListView(ListView):

    model = User
    template_name = 'core/monitores.html'
    # queryset = User.objects.filter(status=True)


class MonitoresDetailView(DetailView):

    model = User
    template_name = 'core/monitores-detail.html'


class MonitoresCreateView(CreateView):

    model = User
    fields = ('registration', 'about', 'first_name', 'last_name', 'password', 'photo', 'username')
    # fields = ('email', 'username', 'password', 'registration', 'about', 'photo')

    template_name = 'core/monitores-form.html'
    success_url = reverse_lazy('monitores')

    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     return super().post(request, *args, **kwargs)


class MonitoresUpdateView(UpdateView):

    model = User
    template_name = 'core/monitores-form.html'


class EventosView(TemplateView):

    template_name = "eventos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
