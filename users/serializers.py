from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.views import ObtainAuthToken

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


class TokenAuthSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'token']
        extra_kwargs = {'email': {'validators': [], 'write_only': True}, 'password': {'write_only': True}}

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs['email'])
        except User.DoesNotExist:
            raise ValidationError(detail="Email or password invalid", code='email_or_password_invalid')
        if user.check_password(attrs['password']):
            token = Token.objects.get_or_create(user=user)[0]
            attrs['token'] = token.key
            return attrs['token', 'email', 'user_id']
        raise ValidationError(detail="Email or password invalid", code='email_or_password_invalid')

class GetUserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['email', '']

