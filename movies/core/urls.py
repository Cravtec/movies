from django.urls import path

from .views import MovieView, MovieCreateView, MovieUpdateView, MovieDeleteView, MovieDetailView


app_name = 'core'
urlpatterns = [
    path('movie/list/', MovieView.as_view(), name='movie_list'),
    path('movie/<int:pk>/detail/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    ]
