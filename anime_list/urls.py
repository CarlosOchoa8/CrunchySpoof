from django.urls import path, include
from .views import AnimeView

urlpatterns = [
    path('anime/create/', AnimeView.as_view()),
    path('anime/read-all/', AnimeView.as_view())
]
