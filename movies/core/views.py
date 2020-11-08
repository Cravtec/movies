import logging
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import MovieForm
from .models import Movie, AGE_CHOICES


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


LOGGER = logging.getLogger()


class MovieView(LoginRequiredMixin, ListView):
    template_name = 'core/movie_list.html'
    model = Movie

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['limits'] = AGE_CHOICES
        print('\n\n\n', result)
        return result
    # extra_context = {'movies': Movie.objects.exclude(genre__age_limit=AGE_CHOICES.adults)}


class MovieCreateView(LoginRequiredMixin, CreateView):
    title = 'Add Movie'
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def from_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView, PermissionRequiredMixin, StaffRequiredMixin):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieDeleteView(LoginRequiredMixin, DeleteView, PermissionRequiredMixin, StaffRequiredMixin):
    template_name = 'core/movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('core:movie_list')

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser


class MovieDetailView(DetailView):
    template_name = 'core/movie_detail.html'
    model = Movie


def confirm_delete(request):
    return render(request, 'core/movie_confirm_delete.html')
