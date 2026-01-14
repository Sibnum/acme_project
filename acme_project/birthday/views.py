from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.urls import reverse_lazy

from .utils import calculate_birthday_countdown
from .models import Birthday
from .forms import BirthdayForm


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(CreateView, LoginRequiredMixin):
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView, LoginRequiredMixin):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(DeleteView, LoginRequiredMixin):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context


@login_required
def simple_view(request):
    return HttpResponse('Страница для залогиненных пользователей!')