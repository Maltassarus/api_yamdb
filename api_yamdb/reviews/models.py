from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        related_name='Reviews',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        related_name='Reviews',
        on_delete=models.CASCADE,
        null=False
    )
    score = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
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
