from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import status
from .serializers import RateAnimeSerializer, AddRateAnimeSerializer
from .models import AnimeScore
from rest_framework_simplejwt.authentication import JWTAuthentication


class RateAnimeView(APIView):

    def post(self, request):
        serializer = AddRateAnimeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        user = request.user
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadAllAnimeRatedView(ListAPIView):
    serializer_class = RateAnimeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['anime']
    queryset = AnimeScore.objects.all()
