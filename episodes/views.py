from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import AddEpisodeSerializer, EpisodeSerializer,\
    ListEpisodeSerializer, UpdateEpisodeSerializer
from .models import Episode


class UploadAnimeView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AddEpisodeSerializer
    queryset = Episode.objects.all()


class ListEpisodesAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListEpisodeSerializer
    queryset = Episode.objects.all()


class EpisodeDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.filter()


class EpisodeUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateEpisodeSerializer
    queryset = Episode.objects.filter()

    # def get_queryset(self):
    #     return self.get_serializer().Meta.model.objects.filter()
    #
    # def patch(self, request, pk=None):  # Funcionamiento interno en Django utilizando patch para obtener registro
    #     anime = self.get_queryset().filter(id=pk).first()  # Obtencion de instancia
    #     if anime:
    #         anime_serializer = self.get_serializer(anime)  # Creacion/validacion de serializador
    #         return Response(anime_serializer.data, status=status.HTTP_200_OK)  #  Se manda serializador
    #     return Response({"error": "No existe un anime con esos datos."}, status=status.HTTP_400_BAD_REQUEST)
