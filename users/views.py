from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer


class UserAPIViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = UserDetailSerializer
        return super().retrieve(request, *args, **kwargs)
