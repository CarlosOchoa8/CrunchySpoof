from django.db import models
from django.db.models import CASCADE
from anime_genre.models import Genre


class Anime(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField()
    genre = models.ForeignKey(Genre, on_delete=CASCADE, null=False)
