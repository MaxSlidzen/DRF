from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserAPIViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
