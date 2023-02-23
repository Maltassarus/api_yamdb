from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from reviews.models import Comment, Review, Title
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
        write_only=True,
    )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    title = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Title.objects.all()
    )

    def validate(self, attrs):
        if self.context['request'].method != 'POST':
            return attrs

        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        user = self.context['request'].user

        if Review.objects.filter(
            author=user,
            title=title
        ).exists():
            raise serializers.ValidationError(
                'Отзыв уже написан'
            )
        return attrs

    class Meta:
        model = Review
        fields = '__all__'
