from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg
from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True
    )
    slug = models.SlugField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True
    )
    slug = models.SlugField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True
    )
    year = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='titles',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(Genre)

    @property
    def rating(self):
        value = self.reviews.all().aggregate(
            Avg('score')).get('score__avg')
        if value:
            return int(value)
        return None

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        related_name='reviews',
        on_delete=models.CASCADE,
        null=False
    )
    score = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Минимальное значение 1'),
            MaxValueValidator(10, 'Максимальное значение 10')
        ]
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True
    )


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
        Review,
        related_name='comments',
        on_delete=models.CASCADE
    )
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
