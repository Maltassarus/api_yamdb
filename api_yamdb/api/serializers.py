from rest_framework import serializers
from django.shortcuts import get_object_or_404

from reviews.models import Comment, Review, Title


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
