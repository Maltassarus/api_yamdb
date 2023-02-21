from dataclasses import field
from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueTogetherValidator


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username',)
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email'],
                message='Пользователь с такими данными уже существует.'
            )
        ]

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'Использовать имя \'me\' в качестве username запрещено.'
            )
        return username
