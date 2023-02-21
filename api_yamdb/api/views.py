from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from users.models import User
from .serializers import SignUpSerializer


class SignUpViewSet(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    pass
