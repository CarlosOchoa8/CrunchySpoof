from django.urls import path, include
from .views import RegisterUser

urlpatterns = [
    path('Auth/UserRegister/', RegisterUser.as_view())
]
