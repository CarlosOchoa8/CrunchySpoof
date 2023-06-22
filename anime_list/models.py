from django.db import models
from django.db.models import CASCADE


class Anime(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='anime_list/anime_imgs/')
    genre = models.JSONField(default=list)
