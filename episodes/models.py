import os
from django.db import models
from django.db.models import CASCADE
from users.models import User
from anime_list.models import Anime


def upload_episode_to(instance, filename):
    anime_name = instance.anime.name
    folder_path = f'anime_list/{anime_name}/episodes/'
    os.makedirs(folder_path, exist_ok=True)
    _, ext = os.path.splitext(filename)
    return f'{folder_path}/{filename}{ext}'


def upload_episode_image_to(instance, image_file):
    anime_name = instance.anime.name
    folder_path = f'anime_list/{anime_name}/episodes/'
    return f'{folder_path}/{image_file}'


class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    episode = models.FileField(upload_to=lambda instance, filename: upload_episode_to(instance, filename))
    comment = models.JSONField(default=list)
    score = models.ForeignKey(User, on_delete=CASCADE)
    image = models.ImageField(upload_to=lambda instance, image_file: upload_episode_image_to(instance, image_file))
