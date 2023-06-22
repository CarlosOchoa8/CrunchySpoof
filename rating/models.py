from django.db import models
from django.db.models import CASCADE
from anime_list.models import Anime
from users.models import User


class AnimeScore(models.Model):
    anime = models.ForeignKey(Anime, on_delete=CASCADE)
    rating = models.FloatField()
    user = models.ForeignKey(User, on_delete=CASCADE)
