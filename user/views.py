from rest_framework.viewsets import ModelViewSet

from .serializers import (
    User, UserSerializer
)

class UserView(ModelViewSet):
    class Meta:
        queryset = User.objects.all()
        serializer_class = UserSerializer