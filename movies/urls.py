from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    # ex: /movie/5/
    path('<int:movie_id>/', views.detail, name='detail'),
    path('actor/<int:actor_id>/', views.actor, name='actor'),
    # ex: /movie/5/vote/
    path('vote/', views.vote, name='vote'),
    path('choose_movie/', views.choose_movie, name='choose_movie'),
    path('results/', views.results, name='results'),
]