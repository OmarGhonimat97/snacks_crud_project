from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Snack
# Create your views here.


class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
    context_object_name = 'snacks'


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['name', 'purchaser', 'description']


class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['name', 'purchaser', 'description']


class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snacks_list')

