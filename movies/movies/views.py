from django.views.generic import ListView

from core.models import Movie


class IndexView(ListView):
    template_name = 'index.html'
    model = Movie
