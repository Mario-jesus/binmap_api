# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name']

    def validate_password(self, value):
        return make_password(value)


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                msg = _('No se pudo iniciar sesión con las credenciales proporcionadas.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Debe incluir "email" y "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
