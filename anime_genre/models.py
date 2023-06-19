from django.db import models
from django.db.models import CASCADE
from ..users.models import User
from ..anime_list.models import Anime


class Genre(models.Model):
    name = models.CharField(max_length=100)
    relationated = models.ForeignKey(Anime, on_delete=CASCADE, null=False)
