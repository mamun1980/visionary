from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, Rating
from .forms import MovieForm, MovieRatingForm
from django.contrib.auth import get_user_model

User = get_user_model()


class MovieListView(ListView):
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm

    def get_success_url(self):
        return reverse('movies:movie-list')
    

class MovieDetailView(DetailView):
    model = Movie


class MovieUpdateView(LoginRequiredMixin, FormView):
    form_class = MovieRatingForm
    template_name = 'movies/movie_rating.html'
    def get_success_url(self):
        return reverse('movies:movie-list')

    def get_context_data(self, **kwargs):
        movie_id = self.kwargs['pk']
        movie = Movie.objects.get(id=movie_id)
        kwargs.setdefault("view", self)
        kwargs['object'] = movie
        return kwargs
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        user_id = data.get('user_id')
        movie_id = data.get('movie_id')
        rating = float(data.get('rating'))
        try:
            movie = Movie.objects.get(id=movie_id)
            user = User.objects.get(id=user_id)
            Rating.objects.create(
                user=user,
                movie=movie,
                rating=rating
            )
            return HttpResponseRedirect("/")
        except Exception as e:
            print(e)