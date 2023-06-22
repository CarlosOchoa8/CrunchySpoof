from rest_framework import serializers
from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    # sections =
    class Meta:
        model = Anime
        fields = ['id', 'name', 'description', 'image', 'genre']

