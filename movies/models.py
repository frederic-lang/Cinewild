from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    date_of_movie = models.DateField()
    language = models.CharField(max_length=100)
    movie_type = models.CharField(max_length=100)
    movie_image = models.ImageField(upload_to='movie_image')
    def __str__(self):
        return self.movie_title


class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    movie = models.ManyToManyField(Movie)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    up_votes = models.IntegerField(default=0)
    actor_image = models.ImageField(upload_to='actor_image')
    def __str__(self):
        return self.actor_name
