from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView
from .views import RegisterUser

urlpatterns = [
    path('Auth/UserRegister/', RegisterUser.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshSlidingView.as_view()),
]
