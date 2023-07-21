import os
from rest_framework import serializers
from .models import Episode
from anime_list.serializers import AnimeSerializer
from anime_list.models import Anime


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['anime', 'name', 'description', 'episode', 'comment', 'score', 'image']

    def to_representation(self, instance):
        episode_data = super().to_representation(instance)
        episode_file = episode_data['episode']

        if os.path.exists(episode_file):
            episode_data['episode'] = episode_file
        else:
            episode_data['episode'] = None

        return {
            'anime': instance.anime.name,
            'name': instance.name,
            'description': instance.description,
            'episode': episode_data['episode'],  # HOT FIX para ver el episodio y extraer la info de
            # relacion
            # 'episode': instance.episode  # SUSTITUIR POR ESTA LINEA LA DE ARRIBA
            # 'image': instance.image if instance.image else '',
            'comment': instance.comment,
            # 'score': instance.score.first_name,
            # 'image': instance.image
        }


class AddEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['anime', 'name', 'description', 'episode', 'comment', 'score', 'image']


class UpdateEpisodeSerializer(serializers.ModelSerializer):
    model = Episode
    anime = serializers.PrimaryKeyRelatedField(queryset=Anime.objects.filter(), required=False)
    name = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(max_length=100, required=False)
    episode = serializers.FileField(required=False)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Episode
        fields = ('id', 'anime', 'name', 'description', 'episode', 'image')

    def to_representate(self, instance):
        representation = super().to_representation(instance)
        representation['anime'] = instance.anime.name
        return instance


class ListEpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = ['anime', 'name', 'description', 'episode']

    def to_representation(self, instance):
        episode_data = super().to_representation(instance)
        episode_file = episode_data['episode']

        if os.path.exists(episode_file):
            episode_data['episode'] = episode_file
        else:
            episode_data['episode'] = None

        return {
            'anime': instance.anime.name,
            'name': instance.name,
            'description': instance.description,
            'episode': episode_data['episode'],  # HOT FIX para ver el episodio y extraer la info de
            # relacion
            # 'episode': instance.episode  # SUSTITUIR POR ESTA LINEA LA DE ARRIBA
            # 'image': instance.image if instance.image else '',
        }
