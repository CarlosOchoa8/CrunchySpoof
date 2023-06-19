from django.db import models
from django.db.models import CASCADE
from users.models import User
from anime_genre.models import Genre
from anime_list.models import Anime


class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    episode = models.FileField(upload_to='episodes/caps/')
    comment = models.JSONField(default=list)
    score = models.ForeignKey(User, on_delete=CASCADE)
    image = models.ImageField(upload_to='episode/image/')
    genre = models.ForeignKey(Genre, on_delete=CASCADE, null=False)
