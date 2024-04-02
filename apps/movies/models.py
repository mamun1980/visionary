from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Movie(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    genre = models.CharField(max_length=50, blank=True, null=True)
    rating = models.CharField(max_length=20, blank=True, null=True)
    release_date = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
    @property
    def average_rating(self):
        ratings = self.movie_rating.values()
        nums = len(ratings)
        total_rate = sum([i['rating'] for i in ratings])
        try:
            rate = total_rate/nums
        except:
            rate = 0
        return rate


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_rating')
    rating = models.DecimalField (max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)])

