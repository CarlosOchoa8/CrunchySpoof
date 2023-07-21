from .views import AddEpisodeCommentView, RetrieveEpisodeCommentsAPIView, ListEpisodeCommentsAPIView
from django.urls import path


urlpatterns = [
    path('comment/', AddEpisodeCommentView.as_view(), name='Comment episode',),
    path('retrieve/<int:pk>', RetrieveEpisodeCommentsAPIView.as_view(), name='Retrieve comments'),
    path('list/', ListEpisodeCommentsAPIView.as_view(), name='List comments'),
]
