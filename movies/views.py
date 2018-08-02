from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Movie, Actor


def home(request):
    return render(request, 'movies/base.html')

def about(request):
    return render(request, 'movies/about.html')

def index(request):
    latest_movie_list = Movie.objects.order_by('-pub_date')[:5]
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})

def actor(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    return render(request, 'movies/actor.html', {'actor':actor})

def choose_movie(request):
    movie_list = Movie.objects.all()
    return render(request, 'movies/choose_movie.html', {'movie_list':movie_list})

def vote(request):
    try:
        selected_movie = Movie.objects.get(pk=request.POST['movie'])
    except (KeyError, Movie.DoesNotExist):
        # Redisplay the form.
        return render(request, 'movies/choose_movie.html', {
            'error_message': "You didn't select a movie.",
            'movie_list' : Movie.objects.all()
        })
    else:
        selected_movie.up_votes += 1
        selected_movie.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('movies:results'))

def results(request):
    movie_list = Movie.objects.all()
    return render(request, 'movies/results.html', {'movie_list':movie_list})



