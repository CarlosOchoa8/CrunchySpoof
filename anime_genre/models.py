from django.db import models
from django.db.models import CASCADE
from users.models import User


class Genre(models.Model):
    name = models.JSONField(default=list)
