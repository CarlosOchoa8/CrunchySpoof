from django.urls import path, include
from .views import RateAnimeView, ReadAllAnimeRatedView

urlpatterns = [
    path('anime/rate/', RateAnimeView.as_view()),
    path('anime-rate/read-all/', ReadAllAnimeRatedView.as_view())
]
