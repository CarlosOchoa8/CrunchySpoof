import os
from django.db import models
from django.db.models import CASCADE


def upload_to(instance, filename):
    anime_name = instance.name
    folder_path = f'anime_list/{anime_name}/'
    os.makedirs(folder_path, exist_ok=True)
    _, ext = os.path.splitext(filename)
    return f'{folder_path}/{filename}{ext}'


class Anime(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=lambda instance, image_file: upload_to(instance, image_file))
    genre = models.JSONField(default=list)
