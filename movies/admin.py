from django.contrib import admin

# Register your models here.

from .models import Movie, Actor

admin.site.register(Movie)
admin.site.register(Actor)
