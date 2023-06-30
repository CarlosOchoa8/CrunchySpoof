from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import UploadAnimeView, ListEpisodesAPIView, EpisodeDetailAPIView, EpisodeUpdateAPIView


router_episodes = DefaultRouter()

router_episodes.register(prefix='series', basename='series', viewset=UploadAnimeView)

urlpatterns = [
    path('series/list/', ListEpisodesAPIView.as_view(), name='List of episodes'),
    path('series/retrieve/<int:pk>/', EpisodeDetailAPIView.as_view(), name='Retrieve an episode'),
    path('series/update/<int:pk>/', EpisodeUpdateAPIView.as_view(), name='Update an episode'),
]

urlpatterns += router_episodes.urls
