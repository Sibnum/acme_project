from django.core.paginator import Paginator
from django.views.generic import (
    ListView, CreateView, DeleteView, DetailView, UpdateView
)
from django.urls import reverse_lazy

from .models import Birthday
from .forms import BirthdayForm


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayDetailView(DetailView):
    model = Birthday


class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
    pass


class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    pass


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass
