from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def index(request):
    movie = Movie.get_random()
    context = {
        'movie': movie
    }
    return render(request, 'movierecommend/index.html', context)
