from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddCommentSerializer, CommentSerializer
from .models import EpisodeComment


class AddEpisodeCommentView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AddCommentSerializer(data=request.data, context={'request': request})  # se manda el usuario por medio del context
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Comentario registrado.'}, status=status.HTTP_200_OK)
        return Response({'message': f'{serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveEpisodeCommentsAPIView(RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = EpisodeComment.objects.filter()


class ListEpisodeCommentsAPIView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = EpisodeComment.objects.filter()
