from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.home, name='home'),
    path('/index/', views.index, name='index'),
    # ex: /movie/5/
    path('<int:movie_id>/', views.detail, name='detail'),
    # ex: /movie/5/actors/
    path('<int:movie_id>/actors/', views.actors, name='actors'),
    # ex: /movie/5/vote/
    path('<int:movie_id>/vote/', views.vote, name='vote'),
]