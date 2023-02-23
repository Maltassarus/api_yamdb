from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all())],

    )

    class Meta:
        model = User
        fields = ('email', 'username',)
        extra_kwargs = {
            'username': {
                'required': True,
                'max_length': 150,
            },
        }
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email'],
                message='Пользователь с такими данными уже существует.',
            )
        ]

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'Использовать имя \'me\' в качестве username запрещено.'
            )
        return username



class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        write_only=True,
    )
    confirmation_code = serializers.CharField(
        max_length=8,
        write_only=True
    )
