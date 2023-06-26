from rest_framework import serializers
from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    # sections =
    class Meta:
        model = Anime
        fields = ['id', 'name', 'description', 'image', 'genre']


class UpdateAnimeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(max_length=555, required=False)
    image = serializers.ImageField(required=False)
    genre = serializers.JSONField(default=list, required=False)

    class Meta:
        model = Anime
        fields = ('name', 'description', 'image', 'genre')

