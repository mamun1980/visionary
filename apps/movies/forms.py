from django import forms
from datetime import datetime

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'rating', 'release_date']


class MovieRatingForm(forms.Form):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '0.1', 'min': '0', 'max': '5'}), required=True)
    
    