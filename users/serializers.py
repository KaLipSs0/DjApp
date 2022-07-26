from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def save(self, *args, **kwargs):
        user = User(email=self.validated_data['email'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def authenticate(self, request):
        pass
