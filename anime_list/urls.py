from django.urls import path, include
from .views import AnimeView, AnimeDetailAPIView, AnimeDestroyAPIView, AnimeUpdateAPIView

urlpatterns = [
    path('anime/create/', AnimeView.as_view()),
    path('anime/list/', AnimeView.as_view(), name='Anime list'),
    path('anime/retrieve/<int:pk>/', AnimeDetailAPIView.as_view(), name='Anime retrieve'),
    path('anime/destroy/<int:pk>/', AnimeDestroyAPIView.as_view(), name='Anime destroy'),
    path('anime/update/<int:pk>/', AnimeUpdateAPIView.as_view(), name='Anime update'),
]
