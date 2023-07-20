from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy
  

# Create your views here.


class SnackListView(ListView):
    template_name = 'snack-list.html'
    model = Snack
    context_object_name = 'snacks'


class SnackDetailView(DetailView):
    template_name = 'snacks-detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snacks-create.html'
    model = Snack
    fields = ['name', 'description', 'owner']


class SnackUpdateView(UpdateView):
    template_name = 'snacks-update.html'
    model = Snack
    fields = ['name', 'description', 'owner']


class SnackDeleteView(DeleteView):
    template_name = 'snacks-delete.html'
    model = Snack
    success_url = reverse_lazy('list_view')