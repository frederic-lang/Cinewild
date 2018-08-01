from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse

from .models import Movie, Actor


def home(request):
    return render(request, 'movies/base.html')

def index(request):
    latest_movie_list = Movie.objects.order_by('-pub_date')[:5]
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})

def actors(request, movie_id):
    response = "You're looking at the actors of movie %s."
    return HttpResponse(response % movie_id)

def vote(request, movie_id):
    return HttpResponse("You're voting on movie %s." % movie_id)

