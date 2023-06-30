from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from .serializers import AnimeSerializer, UpdateAnimeSerializer
from .models import Anime


class AnimeView(APIView):
    def post(self, request):
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        anime_list = Anime.objects.all()
        serializer = AnimeSerializer(anime_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnimeDetailAPIView(RetrieveAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.filter()

    def get(self, request, *args, **kwargs):
        anime_id = kwargs.get("pk")
        if not self.is_valid_id(anime_id):
            return self.response_error("ID de anime no válido", status.HTTP_400_BAD_REQUEST)

        return super().get(request, *args, **kwargs)

    def is_valid_id(self, anime_id):
        try:
            int(anime_id)
            return True
        except (ValueError, TypeError):
            return False

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return self.response_error("El anime no existe", status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

    def response_error(self, message, status):
        return Response({"message": message}, status=status)
    # def get_queryset(self):  # Se coloca al utilizar RetrieveView para indicar donde se hara la busqueda
    #     queryset = self.get_serializer().Meta.model.objects.filter()
    #     if not queryset:
    #         data = {
    #             "error": "Objeto no encontrado.",
    #             "error_detail": "Usted no tiene un comercio asignado.",
    #         }
    #         return Response(data, status=status.HTTP_404_NOT_FOUND)  # No devuelve un mensaje personalizado
    #     return self.get_serializer().Meta.model.objects.filter()


class AnimeDestroyAPIView(DestroyAPIView):  # Es eliminacion directa, se borara de la base de datos
    serializer_class = AnimeSerializer
    # queryset = Anime.objects.filter()  # Es posible solo colocar esta linea y realizara la eliminacion

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter()

    def delete(self, request, pk=None):  # Medida para validar que el objeto se elimine de forma logica (no de la DB)
        anime = self.get_queryset().filter(id=pk).first()
        if anime:
            anime._state = False
            anime.save()
            return Response({"message": "Anime eliminado."}, status=status.HTTP_200_OK)
        return Response({"error": "No existe un anime con esos datos."}, status=status.HTTP_400_BAD_REQUEST)


class AnimeUpdateAPIView(UpdateAPIView):
    serializer_class = UpdateAnimeSerializer
    # queryset = Anime.objects.filter()  # Es posible solo colocar esta linea y realizara la actualizacion

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter()

    def patch(self, request, pk=None):  # Funcionamiento interno en Django utilizando patch para obtener registro
        anime = self.get_queryset().filter(id=pk).first()  # Obtencion de instancia
        if anime:
            anime_serializer = self.get_serializer(anime)  # Creacion/validacion de serializador
            return Response(anime_serializer.data, status=status.HTTP_200_OK)  #  Se manda serializador
        return Response({"error": "No existe un anime con esos datos."}, status=status.HTTP_400_BAD_REQUEST)
