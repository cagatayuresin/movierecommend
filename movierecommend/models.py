from random import randint
from django.db import models


class Movie(models.Model):
    tt = models.CharField("TT", max_length=10)
    url = models.CharField("url", max_length=37)
    title = models.CharField("Title", max_length=60)
    IMDb_point = models.CharField("IMDB Point", max_length=3)
    director = models.CharField("Director", max_length=40)
    genres = models.CharField("Genres", max_length=30)
    year = models.CharField("Year", max_length=4)
    duration = models.CharField("Duration", max_length=3)
    poster_url = models.CharField("Poster", max_length=200)

    def __str__(self):
        return f"{self.title} | {self.year} | {self.IMDb_point}"

    def get_random():
        return Movie.objects.order_by("?")[0]
