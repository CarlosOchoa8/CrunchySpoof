from rest_framework import serializers
from .models import EpisodeComment
from episodes.models import Episode
from users.models import User


class AddCommentSerializer(serializers.ModelSerializer):
    episode = serializers.PrimaryKeyRelatedField(queryset=Episode.objects.all())
    content = serializers.CharField(max_length=1000, required=True)

    def validate_episode(self, value):
        return value

    def validate_content(self, value):
        return value

    def validate(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        print(f'content {validated_data["content"]}')

        if not validated_data['episode'] or not validated_data['content']:
            raise serializers.ValidationError("No es posible agregar el comentario.")
        return validated_data

    class Meta:
        model = EpisodeComment
        fields = ['episode', 'content', 'date', 'user']
        read_only_fields = ['user']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeComment
        fields = ['episode', 'content', 'date', 'user']

    def to_representation(self, instance):
        return {
            'episode': instance.episode.name,
            'content': instance.content,
            'date': instance.date,
            'user': f'{instance.user.first_name} {instance.user.last_name}'
        }
