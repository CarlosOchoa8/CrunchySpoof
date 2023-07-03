from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken  # Recibe usuario como parametro y re genera un token
from .models import User
from .serializers import UserSerializer, UserProfileSerializer, CustomTokenObtainPairSerializer


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(  # Devuelve true o false si existe un usuario asociado
            username=username,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserSerializer(user)
                return Response(
                    {'token': login_serializer.validated_data.get('access'),
                     'refresh-token': login_serializer.validated_data.get('refresh'),
                     'user': user_serializer.data,
                     'message': 'Inicio de sesion exitoso',
                     },
                    status=status.HTTP_200_OK
                )
            return Response({'message': 'usuario o contrasenia incorrectos'}, status=status.HTTP_404_NOT_FOUND)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(pk=request.data.get('user',))
        if user:
            RefreshToken.for_user(user)
            return Response({'message': 'Sesion cerrada satisfactoriamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe este usuario'}, status=status.HTTP_404_NOT_FOUND)


class UserView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('pk'):
            try:
                pk = kwargs.get('pk')
                users = User.objects.get(pk=pk)
            except:
                return Response({'detail': 'No se encontro usuario'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(users)
            return Response(serializer.data)
        else:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
