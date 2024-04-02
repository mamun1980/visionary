from django.contrib import admin
from .models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'rating', 'release_date']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'movie', 'rating']
