from django.urls import path, include
from .views import MovieListView, MovieCreateView, MovieDetailView, MovieUpdateView


app_name = 'movies'

urlpatterns = [
    path("", MovieListView.as_view(), name="movie-list"),
    path("create/", MovieCreateView.as_view(), name="movie-create"),
    path("<int:pk>/", MovieDetailView.as_view(), name="movie-details"),
    path("<int:pk>/edit/", MovieUpdateView.as_view(), name="movie-update")
]
