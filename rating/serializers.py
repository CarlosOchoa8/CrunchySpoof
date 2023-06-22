from rest_framework import serializers
from .models import AnimeScore
from anime_list.serializers import AnimeSerializer
from users.serializers import UserProfileSerializer
from users.models import User
from anime_list.models import Anime


class AddRateAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeScore
        fields = ['anime', 'rating', 'user']
        read_only_fields = ['user']

    def validate(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return validated_data


class RateAnimeSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer()  # Se indica que se serealiza el objeto Anime (la relacion es serializada)
    user = UserProfileSerializer()

    class Meta:
        model = AnimeScore
        fields = ['anime', 'rating', 'user']
