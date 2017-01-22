from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView
)

from .serializers import (
    UserCreateSerializer
)

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
