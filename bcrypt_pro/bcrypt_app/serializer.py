from rest_framework import serializers
from bcrypt_app import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserCustomSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email','password','name')


class LoginCustomSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()