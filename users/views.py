from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserRegisterSerializer, UserAuthSerializer
from rest_framework.authentication import BasicAuthentication


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request)


class AuthUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
