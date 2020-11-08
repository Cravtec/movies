from django.urls import path

from .views import (MovieView,
                    MovieCreateView,
                    MovieUpdateView,
                    MovieDeleteView,
                    MovieDetailView,
                    )

app_name = 'core'
urlpatterns = [
    path('list/', MovieView.as_view(), name='movie_list'),
    path('<int:pk>/detail/', MovieDetailView.as_view(), name='movie_detail'),
    path('create/', MovieCreateView.as_view(), name='movie_create'),
    path('<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),
    path('<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    ]
